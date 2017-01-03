"""Pure Python implementation of Pygame/PyGameSDL2's pygame_time.

Original available at:
    github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/pygame_time.pyx

----------------------------------------------------------------------------
           _ _                    _                                _
     /\   | | |                  | |                              | |
    /  \  | | |_ ___ _ __ ___  __| |  ___  ___  _   _ _ __ ___ ___| |
   / /\ \ | | __/ _ \ '__/ _ \/ _` | / __|/ _ \| | | | '__/ __/ _ \ |
  / ____ \| | ||  __/ | |  __/ (_| | \__ \ (_) | |_| | | | (_|  __/_|
 /_/    \_\_|\__\___|_|  \___|\__,_| |___/\___/ \__,_|_|  \___\___(_)

----------------------------------------------------------------------------

PygameSDL2 Notice:
----------------------------------------------------------------------------
# Copyright 2014 Patrick Dawson <pat@dw.is>
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
----------------------------------------------------------------------------
"""


import math
from sdl2 import SDL_Delay, SDL_GetTicks


def wait(milliseconds):
    """..."""
    start = SDL_GetTicks()
    SDL_Delay(int(milliseconds))
    return SDL_GetTicks() - start


def delay(milliseconds):
    """..."""
    return wait(milliseconds)


def get_time():
    """..."""
    return SDL_GetTicks()


def get_delta(t0):
    """..."""
    return SDL_GetTicks() - t0


class Clock:
    """..."""

    def __init__(self):
        """..."""
        self.last = SDL_GetTicks()
        self.last_frames = []
        self.frametime = 0
        self.raw_frametime = 0

    def tick(self, framerate=0):
        """..."""
        now = SDL_GetTicks()
        self.raw_frametime = now - self.last
        while len(self.last_frames) > 9:
            self.last_frames.pop(0)
        if framerate == 0:
            self.last = now
            self.last_frames.append(self.raw_frametime)
            return self.raw_frametime
        frame_duration = 1.0 / framerate * 1000
        if self.raw_frametime < frame_duration:
            delay(frame_duration - self.raw_frametime)
        now = SDL_GetTicks()
        self.frametime = now - self.last
        self.last = now
        self.last_frames.append(self.frametime)
        return self.frametime

    def tick_busy_loop(self, framerate=0):
        """..."""
        return self.tick(framerate)

    def get_time(self):
        """..."""
        return self.frametime

    def get_rawtime(self):
        """..."""
        return self.raw_frametime

    def get_fps(self):
        """..."""
        total_time = sum(self.last_frames)
        average_time = total_time / 1000.0 / len(self.last_frames)
        average_fps = 1.0 / average_time
        return 0 if math.isnan(average_fps) else average_fps
