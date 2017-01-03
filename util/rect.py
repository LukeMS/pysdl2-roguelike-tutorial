"""Modified, pure Python implementation of PyGameSDL2's rect."""

"""
    Original source code available at:
        github.com/
            renpy/pygame_sdl2/blob/master/src/pygame_sdl2/rect.pyx

    Altered source plain mark:
    --------------------------------------------------------------------------
               _ _                    _                                  _
         /\   | | |                  | |                                | |
        /  \  | | |_ ___ _ __ ___  __| |    ___  ___  _   _ _ __ ___ ___| |
       / /\ \ | | __/ _ \ '__/ _ \/ _` |   / __|/ _ \| | | | '__/ __/ _ \ |
      / ____ \| | ||  __/ | |  __/ (_| |   \__ \ (_) | |_| | | | (_|  __/_|
     /_/    \_\_|\__\___|_|  \___|\__,_|   |___/\___/ \__,_|_|  \___\___(_)

    --------------------------------------------------------------------------

    PygameSDL2 Notice / ZLIB License:
    --------------------------------------------------------------------------
    # Original work:
    #    Copyright 2014 Tom Rothamel <tom@rothamel.us>
    #    Copyright 2014 Patrick Dawson <pat@dw.is>
    # Modified work:
    #    Copyright 2017 Lucas Siqueira <lucas.morais.siqueira@gmail.com>
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
    # 2. Altered source versions must be plainly marked as such, and must not
    #    be misrepresented as being the original software.
    # 3. This notice may not be removed or altered from any source
    #    distribution.
    --------------------------------------------------------------------------
"""

from sdl2 import SDL_Rect


def flatten(*args):
    """..."""
    if len(args) == 1:
        return args[0]
    else:
        return args


def to_sdl_rect(rl):
    """Convert `rectlike` to the SDL_Rect `rect`.

    Args:
        rl (tuple|Rect): a rectlike object to be converted, may be a Rect or
        a (x, y, w, h) tuple.
    Returns:
        SDL_Rect
    """
    rl = Rect(rl)
    return SDL_Rect(rl.x, rl.y, rl.w, rl.h)


class Rect:
    """Object for storing rectangular coordinates."""

    def __init__(self, *args):
        """Initialization.

        Rect objects are used to store and manipulate rectangular areas. A
        Rect can be created from a combination of left, top, width, and
        height values. Rects can also be created from python objects that are
        already a Rect or have an attribute named “rect”.

        The Rect functions that change the position or size of a Rect return
        a new copy of the Rect with the affected changes. The original Rect
        is not modified. Some methods have an alternate “in-place” version
        that returns None but effects the original Rect. These “in-place”
        methods are denoted with the “ip” suffix.

        The Rect object has several virtual attributes which can be used to
        move and align the Rect:
        >>> x,y
        >>> top, left, bottom, right
        >>> topleft, bottomleft, topright, bottomright
        >>> midtop, midleft, midbottom, midright
        >>> center, centerx, centery
        >>> size, width, height
        >>> w,h

        All of these attributes can be assigned to:
        >>> rect1.right = 10
        >>> rect2.center = (20,30)

        Assigning to size, width or height changes the dimensions of the
        rectangle; all other assignments move the rectangle without resizing
        it. Notice that some attributes are integers and others are pairs of
        integers.

        If a Rect has a nonzero width or height, it will return True for a
        nonzero test. Some methods return a Rect with 0 size to represent an
        invalid rectangle.

        The coordinates for Rect objects are all integers. The size values
        can be programmed to have negative values, but these are considered
        illegal Rects for most operations.

        There are several collision tests between other rectangles. Most
        python containers can be searched for collisions against a single
        Rect.

        The area covered by a Rect does not include the right- and bottom-
        most edge of pixels. If one Rect’s bottom border is another Rect’s
        top border (i.e., rect1.bottom=rect2.top), the two meet exactly on
        the screen but do not overlap, and rect1.colliderect(rect2) returns
        false.

        The Rect class can be subclassed. Methods such as copy() and move()
        will recognize this and return instances of the subclass. However,
        the subclass’s __init__() method is not called, and __new__() is
        assumed to take no arguments. So these methods should be overridden
        if any extra attributes need to be copied.

        Args.:
            (4 int tuple; e.g. (left, top, width, height)); or
            (2 int tuple, i.e. one tuple for x and y coordinates, another
            for dimensions; e.g. "(left, top), (width, height)"); or
            (Rect, i.e. another Rect to be copied).

        Raises:
            TypeError

        Usage:
            Rect(left, top, width, height) -> Rect
            Rect((left, top), (width, height)) -> Rect
            Rect(object) -> Rect
        """
        len_args = len(args)

        if len_args == 1 and isinstance(args[0], Rect):
            rect = args[0]
            x = rect.x
            y = rect.y
            w = rect.w
            h = rect.h

        elif len_args == 1 and len(args[0]) == 4:
            x, y, w, h = args[0]

        elif len_args == 1 and len(args[0]) == 2:
            x, y = args[0]
            w = 0
            h = 0

        elif len_args == 2:
            x, y = args[0]
            w, h = args[1]

        elif len_args == 4:
            x, y, w, h = args

        else:
            raise TypeError("Argument must be a rect style object.")

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        """..."""
        return "%s(%d, %d, %d, %d)" % (
            self.__class__.__name__, self.x, self.y, self.w, self.h)

    def __str__(self):
        """..."""
        return "%s(x=%d, y=%d, w=%d, h=%d)" % (
            self.__class__.__name__, self.x, self.y, self.w, self.h)

    def __len__(self):
        """..."""
        return 4

    def __iter__(self):
        """..."""
        return iter((self.x, self.y, self.w, self.h))

    def __getitem__(self, key):
        """..."""
        return (self.x, self.y, self.w, self.h)[key]

    def __setitem__(self, key, val):
        """..."""
        if key == 0:
            self.x = val
        elif key == 1:
            self.y = val
        elif key == 2:
            self.w = val
        elif key == 3:
            self.h = val
        else:
            raise IndexError(key)

    @property
    def left(self):
        """..."""
        return self.x

    @left.setter
    def left(self, val):
        self.x = val

    @property
    def top(self):
        """..."""
        return self.y

    @top.setter
    def top(self, val):
        self.y = val

    @property
    def width(self):
        """..."""
        return self.w

    @width.setter
    def width(self, val):
        self.w = val

    @property
    def height(self):
        """..."""
        return self.h

    @height.setter
    def height(self, val):
        self.h = val

    @property
    def right(self):
        """..."""
        return self.x + self.width

    @right.setter
    def right(self, val):
        self.x += val - self.right

    @property
    def bottom(self):
        """..."""
        return self.y + self.height

    @bottom.setter
    def bottom(self, val):
            self.y += val - self.bottom

    @property
    def size(self):
        """..."""
        return (self.w, self.h)

    @size.setter
    def size(self, val):
        self.w, self.h = val

    @property
    def topleft(self):
        """..."""
        return (self.left, self.top)

    @topleft.setter
    def topleft(self, val):
            self.left, self.top = val

    @property
    def topright(self):
        """..."""
        return (self.right, self.top)

    @topright.setter
    def topright(self, val):
            self.right, self.top = val

    @property
    def bottomright(self):
        """..."""
        return (self.right, self.bottom)

    @bottomright.setter
    def bottomright(self, val):
            self.right, self.bottom = val

    @property
    def bottomleft(self):
        """..."""
        return (self.left, self.bottom)

    @bottomleft.setter
    def bottomleft(self, val):
            self.left, self.bottom = val

    @property
    def centerx(self):
        """..."""
        return self.x + (self.w // 2)

    @centerx.setter
    def centerx(self, val):
            self.x += val - self.centerx

    @property
    def centery(self):
        """..."""
        return self.y + (self.h // 2)

    @centery.setter
    def centery(self, val):
            self.y += val - self.centery

    @property
    def center(self):
        """..."""
        return (self.centerx, self.centery)

    @center.setter
    def center(self, val):
            self.centerx, self.centery = val

    @property
    def midtop(self):
        """..."""
        return (self.centerx, self.top)

    @midtop.setter
    def midtop(self, val):
            self.centerx, self.top = val

    @property
    def midleft(self):
        """..."""
        return (self.left, self.centery)

    @midleft.setter
    def midleft(self, val):
            self.left, self.centery = val

    @property
    def midbottom(self):
        """..."""
        return (self.centerx, self.bottom)

    @midbottom.setter
    def midbottom(self, val):
            self.centerx, self.bottom = val

    @property
    def midright(self):
        """..."""
        return (self.right, self.centery)

    @midright.setter
    def midright(self, val):
            self.right, self.centery = val

    def copy(self):
        """Copy the rectangle.

        Returns a new rectangle having the same position and size as the
        original.

        Usage:
            source_rect.copy()

        Returns:
            Rect (a new Rect instance)
        """
        return Rect(self)

    def move(self, *args):
        """Move the rectangle.

        Returns a new rectangle that is moved by the given offset. The x and
        y arguments can be any integer value, positive or negative.

        Usage:
            source_rect.move(x, y)

        Returns:
            Rect (a new Rect instance)

        """
        r = self.copy()
        r.move_ip(*args)
        return r

    def move_ip(self, *args):
        """Move the rectangle, in place.

        The rectangle is moved by the given offset, operating in place. The x
        and y arguments can be any integer value, positive or negative.

        Usage:
            rect.move(x, y)

        Returns:
            None
        """
        x, y = flatten(args)
        self.x += x
        self.y += y

    def inflate(self, *args):
        """Grow or Shrink the rectangle size.

        Usage:
            source_rect.inflate(x, y)

        Returns:
            Rect (a new Rect instance)

        Returns a new rectangle with the size changed by the given offset.
        The rectangle remains centered around its current center. Negative
        values will shrink the rectangle.
        """
        r = self.copy()
        r.inflate_ip(*args)
        return r

    def inflate_ip(self, *args):
        """Grow or shrink the rectangle size, in place.

        The rectangle's size is changed by the given offset, operating in
        place. Negative values will shrink the rectangle.

        Usage:
            rect.inflate(x, y)

        Returns:
            None
        """
        x, y = flatten(args)
        c = self.center
        self.w += x
        self.h += y
        self.center = c

    def clamp(self, other):
        """Move the rectangle inside another.

        Returns a new rectangle that is moved to be completely inside the
        argument Rect. If the rectangle is too large to fit inside, it is
        centered inside the argument Rect, but its size is not changed.

        Usage:
            source_rect.clamp(Rect)

        Returns:
            Rect (a new Rect instance)

        """
        r = self.copy()
        r.clamp_ip(other)
        return r

    def clamp_ip(self, other):
        """Move the rectangle inside another.

        The rectangle is moved to be completely inside the argument Rect,
        operating in place. If the rectangle is too large to fit inside, it
        is centered inside the argument Rect, but its size is not changed.

        Usage:
            rect.clamp(Rect)

        Returns:
            None

        """
        if not isinstance(other, Rect):
            other = Rect(other)

        if self.w > other.w or self.h > other.h:
            self.center = other.center
        else:
            if self.left < other.left:
                self.left = other.left
            elif self.right > other.right:
                self.right = other.right
            if self.top < other.top:
                self.top = other.top
            elif self.bottom > other.bottom:
                self.bottom = other.bottom

    def clip(self, other, y=None, w=None, h=None):
        """Crop a rectangle inside another.

        Returns a new rectangle that is cropped to be completely inside the
        argument Rect. If the two rectangles do not overlap to begin with, a
        Rect with 0 size is returned.

        Usage:
            clip(Rect)

        Returns:
            Rect (a new Rect instance)
        """
        if type(other) == int:
            other = Rect(other, y, w, h)

        if not isinstance(other, Rect):
            other = Rect(other)

        if not self.colliderect(other):
            return Rect(0, 0, 0, 0)

        r = self.copy()

        # Remember that (0,0) is the top left.
        if r.left < other.left:
            d = other.left - r.left
            r.left += d
            r.width -= d
        if r.right > other.right:
            d = r.right - other.right
            r.width -= d
        if r.top < other.top:
            d = other.top - r.top
            r.top += d
            r.height -= d
        if r.bottom > other.bottom:
            d = r.bottom - other.bottom
            r.height -= d

        return r

    def union(self, other):
        """Join two rectangles into one.

        Returns a new rectangle that completely covers the area of the two
        provided rectangles. There may be area inside the new Rect that is
        not covered by the originals.

        Usage:
            source_rect.union(Rect)

        Returns:
            Rect (a new Rect instance)
        """
        r = self.copy()
        r.union_ip(other)
        return r

    def union_ip(self, other):
        """Join two rectangles into one.

        The rectangle is resized to completely cover its original area and
        that of the argument Rect, operating in place. The resized Rect may
        contain areas that were not covered by either the original Rect or
        the argument Rect.

        Usage:
            source_rect.union(Rect)

        Returns:
            None
        """
        if not isinstance(other, Rect):
            other = Rect(other)

        x = min(self.x, other.x)
        y = min(self.y, other.y)
        self.w = max(self.right, other.right) - x
        self.h = max(self.bottom, other.bottom) - y
        self.x = x
        self.y = y

    def unionall(self, other_seq):
        """Join many rectangles into a new one.

        Returns the union of one rectangle with a sequence of many rectangles.

        Usage:
            source_rect.unionall(Rect_sequence)

        Returns:
            Rect (a new Rect instance)
        """
        r = self.copy()
        r.unionall_ip(other_seq)
        return r

    def unionall_ip(self, other_seq):
        """Join many rectangles into one.

        The rectangle is resized to cover its original area and that of the
        passed as argument, operating in place.

        Usage:
            rect.unionall(Rect_sequence)

        Returns:
            None
        """
        for other in other_seq:
            self.union_ip(other)

    def fit(self, other):
        """Resize and move a rectangle with aspect ratio.

        Returns a new rectangle that is moved and resized to fit another. The
        aspect ratio of the original Rect is preserved, so the new rectangle
        may be smaller than the target in either width or height.

        Usage:
            source_rect.fit(Rect)

        Returns:
            Rect (a new Rect instance)

        """
        if not isinstance(other, Rect):
            other = Rect(other)

        # Not sure if this is entirely correct. Docs and tests are ambiguous.
        r = self.copy()
        r.topleft = other.topleft
        w_ratio = other.w / float(r.w)
        h_ratio = other.h / float(r.h)
        factor = min(w_ratio, h_ratio)
        r.w *= factor
        r.h *= factor
        return r

    def normalize(self):
        """Correct negative sizes of the rectangle.

        This will flip the width or height of a rectangle if it has a
        negative size. The rectangle will remain in the same place, with only
        the sides swapped.

        Usage:
            rect.normalize()
        Returns:
            None
        """
        if self.w < 0:
            self.x += self.w
            self.w = -self.w
        if self.h < 0:
            self.y += self.h
            self.h = -self.h
        return self

    def contains(self, other):
        """Test if an argument rectangle is inside the rectangle.

        Returns true when the argument is completely inside the Rect.

        Usage:
            rect.contains(Rect)

        Returns:
            bool
        """
        if not isinstance(other, Rect):
            other = Rect(other)

        return (other.x >= self.x and other.right <= self.right and
                other.y >= self.y and other.bottom <= self.bottom and
                other.left < self.right and other.top < self.bottom)

    def collidepoint(self, x, y):
        """Test if a point is inside a rectangle.

        Returns True if the given point is inside the rectangle. A point
        along the right or bottom edge is not considered to be inside the
        rectangle.

        Args:
            x (int): X (horizontal) coordinate of the point
            y (int): Y (vertical) coordinate of the point

        Usage:
            rect.collidepoint(0, 3)
            rect.collidepoint(x=0, y=3)

        Returns:
            bool
        """
        return (self.right > x >= self.x) and (self.bottom > y >= self.y)

    def colliderect(self, other):
        """Test if two rectangles overlap.

        Returns true if any portion of either rectangle overlap (except the
        top+bottom or left+right edges).

        Usage:
            rect.colliderect(Rect)

        Returns:
            bool
        """
        if not isinstance(other, Rect):
            other = Rect(other)

        return (self.left < other.right and self.top < other.bottom and
                self.right > other.left and self.bottom > other.top)

    def collidelist(self, other_list):
        """Test if the rectangle collide with any rectangle in the list.

        Test whether the rectangle collides with any in a sequence of
        rectangles. The index of the first collision found is returned. If no
        collisions are found an index of -1 is returned.

        Usage:
            rect.collidelist(list)

        Return:
            int (index of first rectangle that collides or -1 none collides)

        """
        for n, other in zip(range(len(other_list)), other_list):
            if self.colliderect(other):
                return n
        return -1

    def collidelistall(self, other_list):
        """Test if all rectangles in a list intersect.

        Returns a list of all the indices that contain rectangles that
        collide with the Rect. If no intersecting rectangles are found, an
        empty list is returned.

        Usage:
            rect.collidelistall(list)

        Return:
            list (i.e. indices of rectangles that collide)
        """
        colliderect = self.colliderect
        ret = [i for i, other in enumerate(other_list) if colliderect(other)]
        return ret

    def collidedict(self, other_dict):
        """Test if one rectangle in a dictionary intersects.

        Returns the key and value of the first dictionary value that collides
        with the Rect. If no collisions are found, None is returned.

        Rect objects are not hashable and cannot be used as keys in a
        dictionary, only as values.

        Usage:
            collidedict(dict)

        Return:
             tuple (key and value of first rect in the dictionary that
            collides)
             None (if no collision is detected)
        """
        for key, val in other_dict.iteritems():
            if self.colliderect(val):
                return key, val
        return None

    def collidedictall(self, other_dict, rects_values=0):
        """Test if one rectangle instersect with others in a dictionary.

        Returns a list of tuples with the key and value of the rectangles in
        the argument dictionary that intersect with the Rect. If no
        collisions are found an empty list is returned.

        Rect objects are not hashable and cannot be used as keys in a
        dictionary, only as values.

        Usage:
            collidedictall(dict)

        Returns:
            list of tuples ([(key, value), ...] with the rectangles that
            collide)
            empty list (if none collide)
        """
        colliderect = self.colliderect
        ret = [(key, val) for key, val in other_dict.items()
               if colliderect(val)]
        return ret

    def gap(self, other):
        """Return a new rectangle representing the gap between two rectangles.

        If the two rectangles overlap a Rect with size 0 is returned.
        """
        if self.colliderect(other):
            return Rect(0, 0, 0, 0)
        x = min(self.right, other.right)
        y = min(self.bottom, other.bottom)
        w = max(self.left, other.left) - x
        h = max(self.top, other.top) - y
        return Rect(x, y, w, h)
