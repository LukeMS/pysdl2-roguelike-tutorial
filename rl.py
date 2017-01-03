"""..."""

from manager import Manager, SceneBase, Resources


class RogueLike(SceneBase):
    """..."""

    def __init__(self, **kwargs):
        """..."""
        super().__init__(**kwargs)
        fname = Resources.get("HalfOgreFighter3.png")
        self.sprite = self.factory.from_image(fname)
        self.sprite.position = (128, 128)

    def on_update(self):
        """..."""
        self.manager.spriterenderer.render(sprites=self.sprite)


if __name__ == '__main__':
    m = Manager(width=288, height=288)
    m.set_scene(scene=RogueLike)
    m.run()
