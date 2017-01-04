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
            """Reference to sdl2_ext2.SpriteFactory instance.

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
            """Reference to sdl2_ext2.Renderer instance.

            Returns:
                Manager.renderer

            """
            return self.manager.renderer

        @property
        def resources(self):
            """Reference to sdl2_ext2.Resources instance.

            Returns:
                Manager.resources

            """
            return self.manager.resources

        @property
        def sdlrenderer(self):
            """Reference to sdl2.SDL_Renderer instance.

            Returns:
                Manager.renderer.sdlrenderer
            """
            return self.manager.renderer.sdlrenderer

        @property
        def spriterenderer(self):
            """Reference to sdl2_ext2.TextureSpriteRenderSystem instance.

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

.. code-block:: python

    if __name__ == '__main__':
        # example, with a borderless yet ugly green window
        m = Manager(window_color=(0, 255, 0, 255))
        m.set_scene(scene=SceneBase)
        m.run()

[[Complete Roguelike Tutorial, using python3+pysdl2, part 0 code|Here]]'s a rundown of the whole code so far.

[[Complete Roguelike Tutorial, using python3+pysdl2, part 1|Go on to the next part]].

[[Category:Developing]]

<center><table border="0" cellpadding="10" cellspacing="0" style="background:#F0E68C"><tr><td><center>
This is part of a series of tutorials; the main page can be found [[Complete Roguelike Tutorial, using python3+pysdl2|here]].
</center></td></tr></table></center>

------

Part 1: Graphics
==================

.. contents:: :local:

Showing the character on screen
-------------------------------

Time to work with ''rl.py'' - the shiny part our game. Create it in the project's folder.

For this step we're going to need a character sprite. Don't worry, we will draw some letters in the tradition of roguelikes later on. But for now lets use an image.
We're using art by David E. Gervais, available [http://pousse.rapiere.free.fr/tome/tiles/DO/tome-domonsterstiles.htm here] under [https://creativecommons.org/licenses/by/3.0/ CC BY 3.0 license]. Specifically we're using ``HalfOgreFighter3.png``, because, well, they look mighty!
Note that those sprites are in 54x54 resolution. And they have a pink background. A [https://github.com/LukeMS/pysdl2-roguelike-tutorial/blob/master/resources/HalfOgreFighter3.PNG proper sized version with transparent background] is available at the project's GitHub. Create a ''resources'' folder and save the image on it. Save the [https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/resources/davir_gervais_tileset.license license] there too, so that we do not forget to give the author its deserved credits.

By now your project's folder should look like this:
.. code-block::

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
      | +-`david_gervais_tileset.license`_
      | |
      | +-`HalfOgreFighter3.png`_
      |
      +-util/
        |
        +-time.py

Because we did some hard work creating our ''Manager'', ''SceneBase'', etc., we won't even need to import sdl2 for this part. All we need is to import those classes (and ''Resources'') from ''manager'':
<div style="padding: 5px; border: solid 1px #C0C0C0; background-color: #F0F0F0"><syntaxhighlight lang="python">
from manager import Manager, SceneBase, Resources
</syntaxhighlight></div>

.. _`david_gervais_tileset.license`: https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/resources/david_gervais_tileset.license
.. _`HalfOgreFighter3.png`: https://github.com/LukeMS/pysdl2-roguelike-tutorial/raw/master/resources/HalfOgreFighter3.png

Let's put inheritance to work by subclassing ''SceneBase'':

.. code-block:: python

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

That would be all for now.
To test, at the end of the ''rl.py'', adding the belo lines and run it:

.. code-block:: python

    if __name__ == '__main__':
        # create a game/Manager instance
        # we're using an arbitrary size to put our half-ogre right in the middle 
        # of the screen
        m = Manager(width=288, height=288)

        # pass our created RogueLike scene to the Manager
        m.set_scene(scene=RogueLike)

        # make it fly!
        m.run()

And now we should be able to see a mighty half-ogre in the middle of a black screen:

[[File:Roguelike_tutorial_pysdl2-part1-character_on_screen.png|center]]

Show me the @!!!
----------------

TODO
