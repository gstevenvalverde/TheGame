import Boy
from IBuilder import IBuilder


class BoyBuilder(IBuilder):
    boy: Boy

    def __init__(self):
        self.X_POS = None
        self.Y_POS = None
        self.image = None
        self.SCREEN = None

    def reset(self):
        self.boy: Boy

    def set_position(self, x, y):
        self.X_POS = x
        self.Y_POS = y

    def set_image(self, dir_images):
        self.image = dir_images

    def set_screen(self, screen):
        self.SCREEN = screen

    def get_result(self):
        product = Boy.Boy(self.X_POS, self.Y_POS, self.SCREEN)
        self.boy = None
        return product

