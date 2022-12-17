from IBuilder import IBuilder


class Director:

    def make_level_1(self, builder: IBuilder, x, y, screen):
        builder.reset()
        builder.set_position(x, y)
        # builder.set_image(images)
        builder.set_screen(screen)
