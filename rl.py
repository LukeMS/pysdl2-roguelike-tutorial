"""..."""

from manager import Manager, SceneBase, Resources


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


if __name__ == '__main__':
    # create a game/Manager instance
    # we're using an arbitrary size to put our half-ogre right in the middle
    # of the screen
    m = Manager(width=288, height=288)

    # pass our created RogueLike scene to the Manager
    m.set_scene(scene=RogueLike)

    # make it fly!
    m.run()
