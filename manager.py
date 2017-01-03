"""Basic scene manager."""

import ctypes
import os

os.environ["PYSDL2_DLL_PATH"] = "C:\\lib\\SDL2-2.0.5-win32-x86"

import sdl2
import sdl2.ext

from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_COLS, SCREEN_ROWS,
                       LIMIT_FPS, TILE_SIZE, WINDOW_COLOR)
from util.time import Clock

RESOURCES = sdl2.ext.Resources(
    os.path.join(os.path.dirname(__file__), "resources"))


class Manager(object):
    """Manage scenes and the main game loop.

    At each loop the events are passed down to the active scene and it's
    update method is called.
    """

    def __init__(
        self, width=None, height=None, cols=None, rows=None, tile_size=None,
        limit_fps=None, window_color=None
    ):
        """Initialization."""
        self.width = width or SCREEN_WIDTH
        self.height = height or SCREEN_HEIGHT
        self.cols = cols or SCREEN_COLS
        self.rows = rows or SCREEN_ROWS
        self.limit_fps = limit_fps or LIMIT_FPS
        self.tile_size = tile_size or TILE_SIZE
        self.window_color = window_color or WINDOW_COLOR
        self.scene = None

        sdl2.ext.init()

        self.window = sdl2.ext.Window(
            "Tiles", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            flags=sdl2.SDL_WINDOW_BORDERLESS)
        self.renderer = sdl2.ext.Renderer(self.window)
        self.factory = sdl2.ext.SpriteFactory(
            sdl2.ext.TEXTURE, renderer=self.renderer)
        self.spriterenderer = self.factory.create_sprite_render_system(
            self.window)

        self.window.show()
        sdl2.SDL_RaiseWindow(self.window.window)
        self.kb_state = KeyboardStateController()
        self.get_mouse_state()
        self.clock = Clock()
        self.alive = True

    def get_mouse_state(self):
        """..."""
        x = ctypes.c_int(0)
        y = ctypes.c_int(0)
        sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
        self._mouse_x = x.value
        self._mouse_y = y.value
        return self._mouse_x, self._mouse_y

    def run(self):
        """Main loop handling events and updates."""
        while self.alive:
            self.clock.tick(self.limit_fps)
            self.on_event()
            self.on_update()

        sdl2.ext.quit()
        return 0

    def on_event(self):
        """Handle the events and distribute them."""
        scene = self.scene

        if scene is None:
            return
        for event in sdl2.ext.get_events():

            # Exit events
            if event.type == sdl2.SDL_QUIT:
                self.alive = False
                return

            if event.type == sdl2.SDL_WINDOWEVENT_FOCUS_GAINED:
                self.on_update()
                continue

            if event.type == sdl2.SDL_MOUSEMOTION:
                x = event.motion.x
                y = event.motion.y
                buttons = event.motion.state
                self._mouse_x = x
                self._mouse_y = y
                dx = x - self._mouse_x
                dy = y - self._mouse_y
                if buttons & sdl2.SDL_BUTTON_LMASK:
                    scene.on_mouse_drag(event, x, y, dx, dy, "LEFT")
                elif buttons & sdl2.SDL_BUTTON_MMASK:
                    scene.on_mouse_drag(event, x, y, dx, dy, "MIDDLE")
                elif buttons & sdl2.SDL_BUTTON_RMASK:
                    scene.on_mouse_drag(event, x, y, dx, dy, "RIGHT")
                else:
                    scene.on_mouse_motion(event, x, y, dx, dy)
                continue
            elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                x = event.button.x
                y = event.button.y

                button_n = event.button.button
                if button_n == sdl2.SDL_BUTTON_LEFT:
                    button = "LEFT"
                elif button_n == sdl2.SDL_BUTTON_RIGHT:
                    button = "RIGHT"
                elif button_n == sdl2.SDL_BUTTON_MIDDLE:
                    button = "MIDDLE"

                double = bool(event.button.clicks - 1)

                scene.on_mouse_press(event, x, y, button, double)
                continue

            elif event.type == sdl2.SDL_MOUSEWHEEL:
                offset_x = event.wheel.x
                offset_y = event.wheel.y
                scene.on_mouse_scroll(event, offset_x, offset_y)
                continue

            mod = self.kb_state.process(event)
            sym = event.key.keysym.sym

            if event.type == sdl2.SDL_KEYUP:
                scene.on_key_release(event, sym, mod)
            elif event.type == sdl2.SDL_KEYDOWN:
                scene.on_key_press(event, sym, mod)
        return

    def on_update(self):
        """Update scene unless specified not to do so."""
        scene = self.scene
        if self.alive:
            self.renderer.clear(self.window_color)
            if scene:
                scene.on_update()
            self.present()

    def present(self):
        """Flip."""
        sdl2.render.SDL_RenderPresent(self.spriterenderer.sdlrenderer)

    def draw_fps(self):
        """Draw the fps display."""
        ms = self.ms
        if self.show_fps and self.scene:
            text = "FPS: %.3d" % ms
            self.scene.draw_fps(text)

    def set_scene(self, scene=None, **kwargs):
        """..."""
        self.scene = scene(manager=self, **kwargs)


class KeyboardStateController:
    """A class that keeps track of keyboard modifiers and locks."""

    __slots__ = ('_alt', '_ctrl', '_shift', 'caps', 'num', 'scroll')

    def __init__(self):
        """Initialization."""
        self._shift = False
        self._ctrl = False
        self._alt = False
        self.caps = False
        self.num = False
        self.scroll = False

    def contains(self, *args):
        """..."""
        d = {arg: True for arg in args}
        return self.combine(**d)

    @property
    def alt(self):
        """..."""
        return self.combine(ctrl=True)

    @property
    def ctrl(self):
        """..."""
        return self.combine(ctrl=True)

    @property
    def shift(self):
        """..."""
        return self.combine(shift=True)

    def combine(self, alt=False, ctrl=False, shift=False):
        """..."""
        return all(
            (self._alt == alt,
             self._ctrl == ctrl,
             self._shift == shift)
        )

    def process(self, event):
        """Process the current event and update the keyboard state."""
        down = True if event.type == sdl2.SDL_KEYDOWN else False
        self._process_mods(event.key.keysym.sym, down)
        if not down:
            self._process_locks(event.key.keysym.sym)
        return self

    def _process_locks(self, key):
        """Process the locks."""
        for lock, sym in (
            ("caps", sdl2.SDLK_CAPSLOCK),
            ("num", sdl2.SDLK_NUMLOCKCLEAR),
            ("scroll", sdl2.SDLK_SCROLLLOCK)
        ):
            if key == sym:
                _prev_lock = getattr(self, lock)
                setattr(self, lock, not _prev_lock)

    def _process_mods(self, key, down):
        """Process the modifiers."""
        for mod, syms in (
            ("_ctrl", (sdl2.SDLK_LCTRL, sdl2.SDLK_RCTRL)),
            ("_shift", (sdl2.SDLK_LSHIFT, sdl2.SDLK_RSHIFT)),
            ("_alt", (sdl2.SDLK_LALT, sdl2.SDLK_RALT))
        ):
            if key in syms:
                setattr(self, mod, down)

    def __getstate__(self):
        """Prevent pickling."""
        return None

    def __repr__(self):
        """Representation of keyboard states."""
        return (
            "alt: %r, ctrl: %r, shift: %r, caps: %r, num: %r, scroll %r" %
            (self.alt, self.ctrl, self.shift, self.caps, self.num,
             self.scroll))


class SceneBase(object):
    """Basic scene of the game.

    New Scenes should be subclasses of SceneBase.
    """

    def __new__(cls, manager, **kwargs):
        """Create a new instance of a scene.

        A reference to the manager is stored before returning it.

        Args:
            manager (Manager): the running instance of the Manager
        """
        scene = super().__new__(cls)
        scene.manager = manager
        return scene

    def __init__(self, **kwargs):
        """Initialization."""
        pass

    # properties
    @property
    def height(self):
        """Main window height."""
        return self.manager.height

    @property
    def width(self):
        """Main window width."""
        return self.manager.width

    # other methods
    def quit(self):
        """Stop the manager main loop."""
        self.manager.alive = False

    # event methods
    def on_key_press(self, event, sym, mod):
        """Called on keyboard input, when a key is **held down**.

        Args:
            event (sdl2.events.SDL_Event): The base event, as passed by SDL2.
                Unless specifically needed, sym and mod should be used
                instead.
            sym (int): Integer representing code of the key pressed. For
                printable keys ``chr(key)`` should return the corresponding
                character.
            mod (KeyboardStateController): the keyboard state for modifiers
                and locks. See :class:KeyboardStateController
        """
        pass

    def on_key_release(self, event, sym, mod):
        """Called on keyboard input, when a key is **released**.

        By default if the Escape key is pressed the manager quits.
        If that behaviour is desired you can call ``super().on_key_release(
        event, sym, mod)`` on a child class.

        Args:
            event (sdl2.events.SDL_Event): The base event, as passed by SDL2.
                The other arguments should be used for a higher level
                interaction, unless specifically needed.
            sym (int): Integer representing code of the key pressed. For
                printable keys ``chr(key)`` should return the corresponding
                character.
            mod (KeyboardStateController): the keyboard state for modifiers
                and locks. See :class:KeyboardStateController
        """
        if sym == sdl2.SDLK_ESCAPE:
            self.quit()

    def on_mouse_drag(self, event, x, y, dx, dy, button):
        """Called when mouse buttons are pressed and the mouse is dragged.

        Args:
            event (sdl2.events.SDL_Event): The base event, as passed by SDL2.
                The other arguments should be used for a higher level
                interaction, unless specifically needed.
            x (int): horizontal coordinate, relative to window.
            y (int): vertical coordinate, relative to window.
            dx (int): relative motion in the horizontal direction
            dy (int): relative motion in the vertical direction
            button (str, "RIGHT"|"MIDDLE"|"LEFT"): string representing the
                button pressed.
        """
        pass

    def on_mouse_motion(self, event, x, y, dx, dy):
        """Called when the mouse is moved.

        Args:
            event (sdl2.events.SDL_Event): The base event, as passed by SDL2.
                The other arguments should be used for a higher level
                interaction, unless specifically needed.
            x (int): horizontal coordinate, relative to window.
            y (int): vertical coordinate, relative to window.
            dx (int): relative motion in the horizontal direction
            dy (int): relative motion in the vertical direction
        """
        pass

    def on_mouse_press(self, event, x, y, button, double):
        """Called when mouse buttons are pressed.

        Args:
            event (sdl2.events.SDL_Event): The base event, as passed by SDL2.
                The other arguments should be used for a higher level
                interaction, unless specifically needed.
            x (int): horizontal coordinate, relative to window.
            y (int): vertical coordinate, relative to window.
            button (str, "RIGHT"|"MIDDLE"|"LEFT"): string representing the
                button pressed.
            double (bool, True|False): boolean indicating if the click was a
                double click.
        """
        pass

    def on_mouse_scroll(self, event, offset_x, offset_y):
        """Called when the mouse wheel is scrolled.

        Args:
            event (sdl2.events.SDL_Event): The base event, as passed by SDL2.
                The other arguments should be used for a higher level
                interaction, unless specifically needed.
            offset_x (int): the amount scrolled horizontally, positive to the
                right and negative to the left.
            offset_y (int): the amount scrolled vertically, positive away
                from the user and negative toward the user.
        """
        pass

    def on_update(self):
        """Graphical logic."""
        pass


if __name__ == '__main__':
    m = Manager(window_color=(0, 255, 0, 255))
    m.set_scene(scene=SceneBase)
    m.run()
