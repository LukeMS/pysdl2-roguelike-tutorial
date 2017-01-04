Table of contents
*****************

.. contents:: :local:

------

Introduction
============

.. contents:: :local:

Welcome!
--------

Welcome to this tutorial! As you probably guessed, the goal is to have a one-stop-shop for all the info you need on how to build a good Roguelike from scratch. We hope you find it useful! But first, some quick Q&A.

Why Python?
-----------

Most people familiar with this language will tell you it's fun!  Python aims to be simple but powerful, and very accessible to beginners.  This tutorial would probably be much harder without it. We insist that you install/use Python 3.x and go through at least the first parts of the `Python Tutorial`_. This tutorial will be much easier if you've experimented with the language first. Remember that the `Python Library Reference`_ is your friend -- the standard library has everything you might need and when programming you should be ready to search it for help on any unknown function you might encounter.


  **Warning**::
    
       This tutorial is for Python 3 only.
       It is strongly recommended you use the Python 3.5 x86 release.

.. _`Python Tutorial`: https://docs.python.org/tutorial/
.. _`Python Library Reference`: https://docs.python.org/library/index.html

Why SDL2?
-----------

Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D. It is used by video playback software, emulators, and popular games including Valve_'s award winning catalog and many `Humble Bundle`_ games.
SDL officially supports Windows, Mac OS X, Linux, iOS, and Android. Support for other platforms may be found in the source code.
SDL is written in C, works natively with C++, and there are bindings available for several other languages, including C# and **Python**.
SDL 2.0 is distributed under the zlib license. This license allows you to use SDL *`freely in any software`_*.

SDL is extensively used in the industry in both large and small projects: MobyGames listed 141 `games using SDL in 2017`_; the SDL website itself `listed around 700 games in 2012`_; important commercial examples are `Angry Birds`_ or `Unreal Tournament`_; Open Source examples are OpenTTD_, `The Battle for Wesnoth`_ or Freeciv_; the PC game Homeworld_ was ported to the Pandora handheld and `Jagged Alliance 2`_ to Android via SDL; applications like the emulators DOSBox_, VisualBoyAdvance_  and ZSNES_ all use SDL; the `Source Engine`_ (on its Linux and Mac versions) and the CryEngine_ uses SDL.

A common misconception is that SDL is a game engine, but this is not true. However, the library is well-suited for building an engine on top of it. And with python and PySDL2 it shouldn't be hard to build it.

.. _Valve: https://valvesoftware.com/
.. _`Humble Bundle`: https://www.humblebundle.com/
.. _`freely in any software`: https://www.libsdl.org/index.php
.. _`games using SDL in 2017`: https://www.mobygames.com/game-group/middleware-sdl/offset,0/so,4d/
.. _`listed around 700 games in 2012`: https://web.archive.org/web/20100629004347/https://www.libsdl.org/games.php?order=name&category=-1&completed=0&os=-1&match_name=&perpage=-1
.. _`Angry Birds`: https://en.wikipedia.org/wiki/Angry_Birds
.. _`Unreal Tournament`: https://en.wikipedia.org/wiki/Unreal_Tournament
.. _OpenTTD: https://en.wikipedia.org/wiki/OpenTTD
.. _`The_Battle_for_Wesnoth`: https://en.wikipedia.org/wiki/The_Battle_for_Wesnoth
.. _Freeciv: https://en.wikipedia.org/wiki/Freeciv
.. _Homeworld: https://en.wikipedia.org/wiki/Homeworld
.. _`Jagged Alliance 2`: https://en.wikipedia.org/wiki/Jagged_Alliance_2
.. _DOSBox: https://en.wikipedia.org/wiki/DOSBox
.. _VisualBoyAdvance: https://en.wikipedia.org/wiki/VisualBoyAdvance
.. _ZSNES: https://en.wikipedia.org/wiki/ZSNES
.. _`Source Engine`: https://en.wikipedia.org/wiki/Source_(game_engine)
.. _CryEngine: https://en.wikipedia.org/wiki/CryEngine

WHat is PySDL2?
---------------

PySDL2 is a wrapper around the SDL2 library. It has no licensing restrictions, nor does it rely on C code, but uses ctypes instead (considering that ctypes is part of Python's standard library, all you need is a python installation and `SDL2 runtime binaries`_.

  **Warning!**   ::
    
       In this tutorial we're using SDL2 version 2.0.5.
       Other versions could work, but this tutorial do not guarantee compatibility with other versions - you're on your own for it.
       
.. _`SDL2 runtime binaries`: https://www.libsdl.org/download-2.0.php

Inspiration for this tutorial
-------------------------------

This tutorial is heavily inspired by the `Complete Roguelike Tutorial, using python+libtcod`_, a tutorial that is great for its simplicity, helping complete noobs to both programming, python and libtcod create something playable.
At first this is more of a port of that tutorial, but should get its own style over time.

.. _`Complete Roguelike Tutorial, using python+libtcod`: https://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod

Start the tutorial
-------------------------------

Follow the first link to get started!


* '''[[Complete Roguelike Tutorial, using python3+pysdl2, part 0|Part 0: Setting up Python+PySDL2; Setting up your project; Creating a scene Manager]]'''
** Create some utility classes: scene manager, base scene, etc.
** Most of the code up to (including) this part can be found [[Complete Roguelike Tutorial, using python3+pysdl2, part 0 code|here]].
** A release with all of the code produced up to (including) this part can also be viewed or downloaded at [https://github.com/LukeMS/pysdl2-roguelike-tutorial/releases/tag/v0.1.1 this tutorial's GitHhub].


* '''[[Complete Roguelike Tutorial, using python3+pysdl2, part 1|Part 1: Graphics]]'''
** Create a simple scene that draws our character to screen (first graphically, using an image; then using a bitmap font, so that we can see our precious "@"); improve that scene so that the character can be moved around with the arrow keys.

------

Part 0: Setting thins up
========================

.. contents:: :local:

Setting things up
-----------------

Python
######

If you haven't already done so, download and install `Python 3.5`_. Any version of Python 3.x up to 3.5.x should be fine, but its not guaranteed to work.

PySDL2 is currently not working with Python 3.6.
This tutorial was written and tested using Windows 7 x64, Python 3.5.2 x86, PySDL2 0.9.5 and SDL2 x86 2.0.5.
It is advisable to go with 32 bit for compatibility's sake.

.. _`Python 3.5`: https://www.python.org/downloads/release/python-352/

PySDL2
######

The easiest way to install PySDL2 is using pip:

.. code-block:: bash
  
  $ python -m pip install pysdl2

If you would like another form of installation you can look for it at `PySDL2's installing instrunctions`_.

.. _`PySDL2's installing instrunctions`: http://pysdl2.readthedocs.io/en/rel_0_9_5/install.html

SDL2
######

Download the latest release of [https://www.libsdl.org/download-2.0.php SDL2] and extract it somewhere. Be warned that both Python and SDL2 must either be <b>both 32 bit</b>, or <b>both 64 bit</b>.  If you get dll loading errors, getting this wrong is the most likely cause. The SDL2 should be added to your PATH environment variable or placed at the project's folder.
Another option is to tell PySDL2 where the library is located. You can do that py adding those lines at the start of your main python file (explained below):

.. code-block:: python
  
  import os
  
  os.environ["PYSDL2_DLL_PATH"] = "C:\\lib\\SDL2-2.0.5-win32-x86"

Choice of code editor
#####################

If you're just starting out with Python, you'll find that many Python coders just use a simple editor and run their scripts from a console to see any debugging output. Most Python coders don't feel the need to use a fancy IDE! On Windows, Notepad++ is an excellent bet; most Linux programmers already have an editor of choice. Almost all editors allow you to configure shortcut keys (like F5 for instance) to quickly run the script you're editing, without having to switch to a console.

Personally I'm using `Sublime Text 3`_ with the installed packages: `Jedi - Python autocompletion`_; `Python Flake8 Lint`_; `Python Improved`_. Coloring, highlighting, linting, extending it pretty much however you want, etc. makes it like work like a fancy IDE - but light.

.. _`Sublime Text 3`: https://www.sublimetext.com/3
.. _`Jedi - Python autocompletion`: https://github.com/srusskih/SublimeJEDI
.. _`Python Flake8 Lint`: https://github.com/dreadatour/Flake8Lint
.. _`Python Improved`: https://github.com/MattDMo/PythonImproved

Setting up your project
-----------------------

Your project folder
#####################

Now create your project's folder. Inside it, create two empty files ''constants.py'' and ''manager.py''.  It'll make the tutorial easier to just use the same names for now, and you can always rename it later.

.. code-block::

+-pysdl2-roguelike-tutorial/
   |
   +-constants.py
   |
   +-manager.py

If you chose to keep the SDL2 library at the project folder, it should now look like this:

.. code-block::

 +-pysdl2-roguelike-tutorial/
   |
   +-constants.py
   |
   +-manager.py
   |
   +-README-SDL.txt
   |
   +-SDL2.dll (.dll for Windows, .so for Linux).

We will omit the sdl library and txt from now on when we list the folder's content. If you have it, just remember that you will have those two additional files on top of what is shown.

You're ready to start editing stuff!

Defining constants
#####################

It's good practice to define constants, special numbers that might get reused. ''Constants are usually defined on a module level and written in all capital letters with underscores separating words'', according to `Python's style guide`_ - its not required, but it should make your code more readable to other people, so we're sticking to this style. Let's create a file named ''constants.py'' at our project's folder and write on it:

.. code-block:: python

	"""Game constants."""

	# size of a (square) tile's side in pixels.
	TILE_SIZE = 32

	# the width of the screen in pixels.
	SCREEN_WIDTH = 1024

	# the height of the screen in pixels
	SCREEN_HEIGHT = 768

	# maximum frames per second that should be drawn
	LIMIT_FPS = 30

	# the window's background color (RGBA, from 0-255)
	WINDOW_COLOR = (0, 0, 0, 255)

Now that we have our contants defined is time to create our scene manager!

.. _`Python's style guide`: https://www.python.org/dev/peps/pep-0008/


Creating a scene Manager
------------------------

Wait, manager? Ain't we making a game?
SDL2 is a C library. PySDL2 is a python wrapper for that library. But remember we've said at the introduction that SDL2 is not a game engine? Neither is PySDL2, although it does provide higher level classes and methods to help us.
We're going to create some classes to make our lives easier, more like a python game engine, less like a bunch of C methods. It will take some time until we can finally draw our character to the screen, but it will save us lots of re-work in the future.
If you don't care about the implementation of the ''Manager'' and related classes, our boilerplate code, you can just download the [https://github.com/LukeMS/pysdl2-roguelike-tutorial/releases/tag/v0.1.1 0.x release] (part 0 of the tutorial = 0.x releases) of the project on GitHub and skip to the [[Complete Roguelike Tutorial, using python3+pysdl2, part 1|Part 1]]. The code should be reasonably well described, with lots of docstrings and comments (feel free file an issue on GitHub if something is not described well enough) so that you may be able to understand it all just by looking at (actually, reading) it. And you can always come back here if, on the later stages, you feel like you need to understand what's going on in that ''manager.py''.
But even before we deal with the ''Manager'', we're going to work on a ''Clock'', the class that will control our frame rate among time. Something that the ''Manager'' itself will depend on.

Tick the Clock
#####################

Pygame, a python library based on SDL version 1.x, had a Clock. There is another library, based on Pygame, that is built around SDL2, named pygame-sdl2, that has a [https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/pygame_time.pyx Clock], but it's made using  cython, not python (this could actually be considered good, considering performance, but at this tutorial we're aiming at pure Python, because one language is enough for a tutorial). We're not reinventing the wheel, but we're adapting that cython Clock to a python one. We're not going to dive deeper into this process, just know that [https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/util/time.py this] is a pure Python port of [https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/pygame_time.pyx that].
You should download the ported version we're going to use from [https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/util/time.py here]. Make sure its placed under ''util/time.py'' in your project's folder.
*Note*: pygame-sdl2's code is released under zlib license. That means you can do almost everything you want with it, but it remains a copyrighted work. That being said, you can use it, even commercially, but we're not going to place the code here. Just get it through git and use it.

Now we're going to work on ''manager.py''.

Creating the Manager
#####################

Firt of all we're going to need a few imports:

.. code-block:: python

    # ctypes will be required for a single use at startup, don't let it scare you!
    import ctypes
    import os

    # tell sdl2 where your library is
    os.environ["PYSDL2_DLL_PATH"] = "C:\\lib\\SDL2-2.0.5-win32-x86"

    # import sdl2
    import sdl2
    # and sdl2.ext, where the pythonic part of the pysdl2 resides
    import sdl2.ext

    # import the constants we've defined
    from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, LIMIT_FPS,
                           WINDOW_COLOR)

    # impor our pythonic Clock
    from util.time import Clock
 
Next we're going to instantiate sdl2.ext.Resources to help us handling our resources:

.. code-block:: python

	    Resources = sdl2.ext.Resources(
        os.path.join(os.path.dirname(__file__), "resources"))

Then we're going to create the Manager class. As the first lines of its initialization we're going to unpack some arguments related to the constants we've defined. The description should make it clear enough:

.. code-block:: python

    class Manager(object):
        """Manage scenes and the main game loop.

        At each loop the events are passed down to the active scene and it's
        update method is called.
        """

        def __init__(
            self, width=None, height=None, cols=None, rows=None, tile_size=None,
            limit_fps=None, window_color=None
        ):
            """Initialization.

            Args:
                width (int): the width of the screen in pixels. Defaults to
                    constants.SCREEN_WIDTH
                height (int): the height of the screen in pixels. Defaults to
                    constants.SCREEN_HEIGHT
                tile_size (int): size of a (square) tile's side in pixels.
                    Defaults to constants.TILE_SIZE
                limit_fps (int): maximum frames per second that should be drawn.
                    Defaults to constants.LIMIT_FPS
                window_color (4-tuple): the window's background color, as a tuple
                    of 4 integers representing Red, Greehn, Blue and Alpha values
                    (0-255). Defaults to constants.WINDOW_COLOR

            Usage:
                m = Manager()  # start with default parameters
                m.set_scene(SceneBase)  # set a scene. This is a blank base scene
                m.execute()  # call the main loop
            """
            # Set the default arguments
            self.width = width or SCREEN_WIDTH
            self.height = height or SCREEN_HEIGHT
            self.tile_size = tile_size or TILE_SIZE
            self.limit_fps = limit_fps or LIMIT_FPS
            self.window_color = window_color or WINDOW_COLOR

            # Number of tile_size-sized drawable columns and rows on screen
            self.cols = self.width // self.tile_size
            self.rows = self.height // self.tile_size

The way we've built our Manager so far allow us to consider the constants as default values but still accept values passed in during its initialization. An example of that will be shown when we first draw our character.
We're also going to set a blank scene (''None'') at start, requiring that, after the Manager instantiation, a proper scene is passed to it before starting the main loop (unless you want't to stare at blank scrren).

.. code-block:: python

            ...
            # Initialize with no scene
            self.scene = None

And finally we're going to write some SDL stuff, mostly via PySDL2.ext utilities, so that we don't have to it on each scene we create:

.. code-block:: python

        ...
        # Initialize the video system - this implicitly initializes some
        # necessary parts within the SDL2 DLL used by the video module.
        #
        # You SHOULD call this before using any video related methods or
        # classes.
        sdl2.ext.init()

        # Create a new window (like your browser window or editor window,
            # etc.) and give it a meaningful title and size. We definitely need
            # this, if we want to present something to the user.
            self.window = sdl2.ext.Window(
                "Tiles", size=(self.width, self.height),
                flags=sdl2.SDL_WINDOW_BORDERLESS)

            # Create a renderer that supports hardware-accelerated sprites.
            self.renderer = sdl2.ext.Renderer(self.window)

            # Create a sprite factory that allows us to create visible 2D elements
            # easily.
            self.factory = sdl2.ext.SpriteFactory(
                sdl2.ext.TEXTURE, renderer=self.renderer)

            # Creates a simple rendering system for the Window. The
            # SpriteRenderSystem can draw Sprite objects on the window.
            self.spriterenderer = self.factory.create_sprite_render_system(
                self.window)

            # By default, every Window is hidden, not shown on the screen right
            # after creation. Thus we need to tell it to be shown now.
            self.window.show()

            # Enforce window raising just to be sure.
            sdl2.SDL_RaiseWindow(self.window.window)

            # Initialize the keyboard state controller.
            # PySDL2/SDL2 shouldn't need this but the basic procedure for getting
            # key mods and locks is not working for me atm.
            # So I've implemented my own controller.
            self.kb_state = KeyboardStateController()

            # Initialize a mouse starting position. From here on the manager will
            # be able to work on distances from previous positions.
            self._get_mouse_state()

            # Initialize a clock utility to help us control the framerate
            self.clock = Clock()

            # Make the Manager alive. This is used on the main loop.
            self.alive = True

        def _get_mouse_state(self):
            """Get the mouse state.

            This is only required during initialization. Later on the mouse
            position will be passed through events.
            """
            # This is an example of what PySDL2, below the hood, does for us.
            # Here we create a ctypes int (i.e. a C type int)
            x = ctypes.c_int(0)
            y = ctypes.c_int(0)
            # And pass it by reference to the SDL C function (i.e. pointers)
            sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
            # The variables were modified by SDL, but are still of C type
            # So we need to get their values as python integers
            self._mouse_x = x.value
            self._mouse_y = y.value
            # Now we hope we're never going to deal with this kind of stuff again
            return self._mouse_x, self._mouse_y

The long comments and docstring should provide some information about what we just did.
We initialize SDL2 (''sdl2.ext.init()''); create a (borderless, in this case) window (''sdl2.ext.Window'');  create a renderer that supports hardware acceleration (sdl2.ext.Renderer; it uses textures instead of surfaces, works with/on the GPU and provides a nice performance gain, should you require it for drawing tons of sprites); we also create a sprite factory (''sdl2.ext.SpriteFactory'') that will help make sprite creation easier for us later on; we ask the window to be shown (''window.show()'') and raised (''sdl2.SDL_RaiseWindow(window)'') in case some input got our focus; we instantiate a ''KeyboardStateController'' what will be described below (because the default PySDL2 way of handling keyboard mods and locks, although easier in theory, simply doesn't work for my computer/keyboard); then we get our initial mouse state (starting position); finally we instantiate our Clock and set the Manager state to alive!

Now we have to create our main loop that will keep the game running, process and dispatch events (input and output events). We keep it small and call other helper functions to do specialized work:

.. code-block:: python

        def run(self):
            """Main loop handling events and updates."""
            while self.alive:
                self.clock.tick(self.limit_fps)
                self.on_event()
                self.on_update()
            return sdl2.ext.quit()

The ''on_event'' method takes a bit more of work to evaluate the events received and dispatch them accordingly (mouse events, keyboard events and its specific types such as press/release/etc.):

.. code-block:: python

        def on_event(self):
            """Handle the events and pass them to the active scene."""
            scene = self.scene

            if scene is None:
                return
            for event in sdl2.ext.get_events():

                # Exit events
                if event.type == sdl2.SDL_QUIT:
                    self.alive = False
                    return

                # Redraw in case the focus was lost and now regained
                if event.type == sdl2.SDL_WINDOWEVENT_FOCUS_GAINED:
                    self.on_update()
                    continue

                # on_mouse_motion, on_mouse_drag
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
                # on_mouse_press
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
                # on_mouse_scroll (wheel)
                elif event.type == sdl2.SDL_MOUSEWHEEL:
                    offset_x = event.wheel.x
                    offset_y = event.wheel.y
                    scene.on_mouse_scroll(event, offset_x, offset_y)
                    continue

                # for keyboard input, set the key symbol and keyboard modifiers
                mod = self.kb_state.process(event)
                sym = event.key.keysym.sym

                # on_key_release
                if event.type == sdl2.SDL_KEYUP:
                    scene.on_key_release(event, sym, mod)
                # on_key_press
                elif event.type == sdl2.SDL_KEYDOWN:
                    scene.on_key_press(event, sym, mod)
                    
So what we've done here is: check the type of the event and deliver it to whatever method we're going to create on the game scenes to handle that type of event.
The output (graphic) part is simpler:

.. code-block:: python

        def on_update(self):
            """Update the active scene."""
            scene = self.scene
            if self.alive:
                # clear the window with its color
                self.renderer.clear(self.window_color)
                if scene:
                    # call the active scene's on_update
                    scene.on_update()
                # present what we have to the screen
                self.present()

        def present(self):
            """Flip the GPU buffer."""
            sdl2.render.SDL_RenderPresent(self.spriterenderer.sdlrenderer)

And finally we need to set up each scene that we pass to the Manager:

.. code-block:: python

        def set_scene(self, scene=None, **kwargs):
            """Set the scene.

            Args:
                scene (SceneBase): the scene to be initialized
                kwargs: the arguments that should be passed to the scene

            """
            self.scene = scene(manager=self, **kwargs)

keyboard state controller
#########################

The ''KeyboardStateController'' class will keep track of two things: if ''alt'', ''ctrl'' and/or ''shift'' are held; if ''caps'', ''num'' and/or ''scroll lock'' are on/off.
As I've said above the default SDL2/PySDL2 way of handling this simpy don't work for me, thus a new way of tracking needs to be created:

.. code-block:: python

    class KeyboardStateController:
        """A class that keeps track of keyboard modifiers and locks."""

        def __init__(self):
            """Initialization."""
            # evernthing defaults to False
            self._shift = False
            self._ctrl = False
            self._alt = False
            self.caps = False
            self.num = False
            self.scroll = False

        @property
        def alt(self):
            """Evaluate if the alt key only is held."""
            return self.combine(ctrl=True)

        @property
        def ctrl(self):
            """Evaluate if the ctrl key only is held."""
            return self.combine(ctrl=True)

        @property
        def shift(self):
            """Evaluate if the ctrl key only is held."""
            return self.combine(shift=True)

        def combine(self, alt=False, ctrl=False, shift=False):
            """Evaluate key combinations."""
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

No need to go into details here: it process an  event and set its state accordingly. We can check for simple mods (e.g. ''kb_state.shift'') or locks (e.g. ''kb_state.caps'') or multiple mods (''kb_state.combine(shift=True, ctrl=True)'').

Creating a base scene
#####################

Every line that we write here is a line that we won't have to write at each scene later on. Don't give up! We're gaining in the long term.
We should now create a base scene that would be inherited by the custom scenes we create. This scene should know who is its Manager and be able to access some of its attributes and methods easily. And it should act show how input and output are usually handled/passed by the Manager. Some of the properties here might not be used by you at all. But know that, if you need it, most of the essential ones are here. And as usual we're hoping the dosctrings and comments help explain what we forget:

.. code-block:: python

class SceneBase(object):
    """Basic scene of the game.

    New Scenes should be subclasses of SceneBase.
    """

    def __new__(cls, manager, **kwargs):
        """Create a new instance of a scene.

        A reference to the manager is stored before returning the instance.
        This is made preventively because many properties are related to the
        manager.

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
        """Main window height.

        Returns:
            Manager.height
        """
        return self.manager.height

    @property
    def width(self):
        """Main window width.

        Returns:
            Manager.height
        """
        return self.manager.width

    @property
    def factory(self):
        """Reference to sdl2.ext.SpriteFactory instance.

        Returns:
            Manager.factory
        """
        return self.manager.factory

    @property
    def kb_state(self):
        """Reference to KeyboardStateController instance.

        Returns:
            Manager.kb_state
        """
        return self.manager.kb_state

    @property
    def renderer(self):
        """Reference to sdl2.ext.Renderer instance.

        Returns:
            Manager.renderer

        """
        return self.manager.renderer

    @property
    def sdlrenderer(self):
        """Reference to sdl2.SDL_Renderer instance.

        Returns:
            Manager.renderer.sdlrenderer
        """
        return self.manager.renderer.sdlrenderer

    @property
    def spriterenderer(self):
        """Reference to sdl2.ext.TextureSpriteRenderSystem instance.

        Returns:
            Manager.spriterenderer
        """
        return self.manager.spriterenderer

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

Ta-da! No, no character on screen yet. But things are about to start running smoothly from now on!
To test if everything works so far, add the lines below to the end of ''manager.py''. Cross your fingers and run it!
An ugly green screen should appear and, if you press Escape, it should quit quietly.
<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">
if __name__ == '__main__':
    # example, with a borderless yet ugly green window
    m = Manager(window_color=(0, 255, 0, 255))
    m.set_scene(scene=SceneBase)
    m.run()
</syntaxhighlight></div>

[[Complete Roguelike Tutorial, using python3+pysdl2, part 0 code|Here]]'s a rundown of the whole code so far.

[[Complete Roguelike Tutorial, using python3+pysdl2, part 1|Go on to the next part]].

[[Category:Developing]]

<center><table border="0" cellpadding="10" cellspacing="0" style="background:#F0E68C"><tr><td><center>
This is part of a series of tutorials; the main page can be found [[Complete Roguelike Tutorial, using python3+pysdl2|here]].
</center></td></tr></table></center>


__TOC__

<center><h1>'''Graphics'''</h1></center>

== Showing the character on screen ==

Time to work with ''rl.py'' - the shiny part our game. Create it in the project's folder.

For this step we're going to need a character sprite. Don't worry, we will draw some letters in the tradition of roguelikes later on. But for now lets use an image.
We're using art by David E. Gervais, available [http://pousse.rapiere.free.fr/tome/tiles/DO/tome-domonsterstiles.htm here] under [https://creativecommons.org/licenses/by/3.0/ CC BY 3.0 license]. Specifically we're using ``HalfOgreFighter3.png``, because, well, they look mighty!
Note that those sprites are in 54x54 resolution. And they have a pink background. A [https://github.com/LukeMS/pysdl2-roguelike-tutorial/blob/master/resources/HalfOgreFighter3.PNG proper sized version with transparent background] is available at the project's GitHub. Create a ''resources'' folder and save the image on it. Save the [https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/resources/davir_gervais_tileset.license license] there too, so that we do not forget to give the author its deserved credits.

By now your project's folder should look like this:
 +-pysdl2-roguelike-tutorial/
   |
   +-constants.py
   |
   +-manager.py
   |
   +-rl.py
   |
   +-resources/
   | |
   | +-[https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/resources/davir_gervais_tileset.license davir_gervais_tileset.license]
   | |
   | +-[https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/resources/HalfOgreFighter3.png HalfOgreFighter3.png]
   |
   +-util/
     |
     +-time.py

Because we did some hard work creating our ''Manager'', ''SceneBase'', etc., we won't even need to import sdl2 for this part. All we need is to import those classes (and ''Resources'') from ''manager'':
<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">
from manager import Manager, SceneBase, Resources
</syntaxhighlight></div>


Let's put Inheritance to work by subclassing ''SceneBase'':

<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">
class RogueLike(SceneBase):
    """An aspiring Roguelike game's scene."""

    def __init__(self, **kwargs):
        """Initialization."""
        # Nothing there for us but lets call super in case we implement
        # something later on, ok?
        super().__init__(**kwargs)

        # pass the name of the resource to the sdl2.ext.Resources instance on
        # manager.py
        fname = Resources.get("HalfOgreFighter3.png")

        # use the pysdl2 factory to create a sprite from an image
        self.sprite = self.factory.from_image(fname)

        # set it to a position to look better on our screenshot :)
        self.sprite.position = (128, 128)

    def on_update(self):
        """Graphical logic."""
        # use the render method from manager's spriterenderer
        self.manager.spriterenderer.render(sprites=self.sprite)
</syntaxhighlight></div>
That would be all for now.
To test, at the end of the ''rl.py'', adding the belo lines and run it:
<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">
if __name__ == '__main__':
    # create a game/Manager instance
    # we're using an arbitrary size to put our half-ogre right in the middle 
    # of the screen
    m = Manager(width=288, height=288)

    # pass our created RogueLike scene to the Manager
    m.set_scene(scene=RogueLike)

    # make it fly!
    m.run()
</syntaxhighlight></div>

And now we should be able to see a mighty half-ogre in the middle of a black screen:

[[File:Roguelike_tutorial_pysdl2-part1-character_on_screen.png|center]]

== Show me the @!!! ==

In this tutorial we're using a bitmap created from a regular font. I've done this myself and you can download it here.
Now, something libtcod-specific: we're going to use a custom font! It's pretty easy. libtcod comes bundled with a few fonts that are usable right out of the box. Remember however that they can be in different '''formats''', and you'll need to tell it about this. This one is "grayscale" and using the "tcod layout", most fonts are in this format and thus end with ''_gs_tc''. If you wanna use a font with a different layout or make your own, the [http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/console_set_custom_font.html?c=false&cpp=false&cs=false&py=true&lua=false docs on the subject] are really informative. You can worry about that at a later time though. Notice that the size of a font is automatically detected.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)</syntaxhighlight></div>


This is probably the most important call, initializing the window. We're specifying its size, the title (change it now if you want to), and the last parameter tells it if it should be fullscreen or not.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)</syntaxhighlight></div>


For a real-time roguelike, you wanna limit the speed of the game (frames-per-second or FPS). If you want it to be turn-based, ignore this line. (This line will simply have no effect if your game is turn-based.)

<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #D0FFC2"><syntaxhighlight lang="python">libtcod.sys_set_fps(LIMIT_FPS)</syntaxhighlight></div>


Now the main loop. It will keep running the logic of your game as long as the window is not closed.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">while not libtcod.console_is_window_closed():</syntaxhighlight></div>


For each iteration we'll want to print something useful to the window. If your game is turn-based each iteration is a turn; if it's real-time, each one is a frame. Here we're setting the text color to be white. [http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/color.html?c=false&cpp=false&cs=false&py=true&lua=false There's a good list of colors you can use here], along with some info about mixing them and all that. The zero is the console we're printing to, in this case the screen; more on that later.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">    libtcod.console_set_default_foreground(0, libtcod.white)</syntaxhighlight></div>


Don't forget the indentation at the beginning of the line, it's extra-important in Python. '''Make sure you don't mix tabs with spaces for indentation!''' This comes up often if you copy-and-paste code from the net, and you'll see an error telling you something about the indentation (that's a pretty big clue right there!). Choose one option and stick with it. In this tutorial we're using the 4-spaces convention, but tabs are easy to work with in many editors so they're a valid choice too.

Now print a character to the coordinates (1,1). Once more the first zero specifies the console, which is the screen in this case. Can you guess what that character is? No, it doesn't move yet!


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)</syntaxhighlight></div>


At the end of the main loop you'll always need to present the changes to the screen. This is called ''flushing'' the console and is done with the following line.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">    libtcod.console_flush()</syntaxhighlight></div>


Ta-da! You're done. Run that code and give yourself a pat on the back!

<center><table border="0" cellpadding="10" cellspacing="0" style="background:#F0E68C" width="65%"><tr><td><center>
<b>Common reasons the code won't run.</b></center>

* On Windows? Is either of the libtcod or SDL dlls not found?<br/><i>Make sure your Python and libtcod are either BOTH 32 bit, or BOTH 64 bit.</i>
* Python errors? Using Python 3?<br/><i>We said above that this tutorial is only for Python 2.  So use Python 2, with Python 3 you are on your own.  They're different languages, it won't just magically work!</i>
* Still blocked?  Check out the [[Complete_Roguelike_Tutorial,_using_Python+libtcod,_problems|problems page]].
</td></tr></table></center>

Note that since we don't have any input handling code, the game may crash on exit (it won't process the OS's requests to close). Oops! Don't worry though, this problem will go away as soon as we add keyboard support.

[[Complete Roguelike Tutorial, using python+libtcod, part 1 code#Showing the @ on screen|Here]]'s the complete code so far.

== Moving around ==

That was pretty neat, huh? Now we're going to move around that @ with the keys!

First, we need to keep track of the player's position. We'll use these variables for that, and take the opportunity to initialize them to the center of the screen instead of the top-left corner. This can go just before the main loop.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2</syntaxhighlight></div>


There are functions to check for pressed keys. When that happens, just change the coordinates accordingly. Then, print the @ at those coordinates. We'll make a separate function to handle the keys.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">def handle_keys():
    global playerx, playery
    
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1
        
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1
        
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1
        
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1</syntaxhighlight></div>


Done! These are the arrow keys, if you want to use other keys here's a [http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/console_keycode_t.html?c=false&cpp=false&cs=false&py=true&lua=false reference] (pay attention to the Python-specific notes).

While we're at it, why not include keys to toggle fullscreen mode, and exit the game? You can put this at the beginning of the function.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">  
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game</syntaxhighlight></div>


From now on, we'll show code for a <span style="background-color: #D0FFC2">'''real-time game'''</span> with a green background, and code for a <span style="background-color: #DFEEFF">'''turn-based game'''</span> with a blue background.

Notice a subtle difference here. The ''console_is_key_pressed'' function is useful for real-time games, since it checks if a key is pressed with no delays. ''console_check_for_keypress'', on the other hand, treats the key like it's being typed. So after the first press, it will stop working for a fraction of a second. This is the same behavior you see when you type, otherwise pressing a key would result in you typing 3 or 4 letters! It's useful for all commands except movement, which you usually want to react as soon as possible with no delays, and continue for as long as you press the movement keys.

Now here's an important thing: you can use that first line to distinguish between real-time and turn-based gameplay! See, ''console_check_for_keypress'' won't block the game. But if you replace it with this line:

<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #DFEEFF"><syntaxhighlight lang="python">    key = libtcod.console_wait_for_keypress(True)</syntaxhighlight></div>


Then the game won't go on unless the player presses a key. So effectively you have a turn-based game now.

Now, the main loop needs to call this function in order for it to work. If the returned value is True, then we "break" from the main loop, ending the game. The inside of the main loop should now look like this:


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)
    
    libtcod.console_flush()
    
    #handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break</syntaxhighlight></div>


The reason why we draw stuff before handling key input is that, in a turn-based game, the first screen is shown before the first key is pressed (otherwise the first screen would be blank).

One more thing! If you try that, you'll see that moving you leave around a trail of little @'s. That's not what we want! We need to clear the character at the last position before moving to the new one, this can be done by simply printing a space there. Put this just before ''exit = handle_keys()''.


<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">        libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)</syntaxhighlight></div>


[[Complete Roguelike Tutorial, using python+libtcod, part 1 code#Moving around|Here]]'s a rundown of the whole code so far.

[[Complete Roguelike Tutorial, using python+libtcod, part 2|Go on to the next part]].

[[Category:Developing]]



.. code-block:: bash

  pip install pysdl2

.. code-block:: ruby

  @a = "using code-block ruby"
  puts @a
  
.. code-block:: python

  [i for i in range(10)]
