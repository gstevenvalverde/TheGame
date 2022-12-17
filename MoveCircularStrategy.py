import math
from abc import ABC

import IStrategy


class MoveCircularStrategy(IStrategy.IStrategy):

    def __init__(self):
        self.angle = 0
        self.X_POS = 0
        self.Y_POS = 0
        self.rect = None

    def execute(self, x, y, rect):
        # self.X_POS = x
        # self.Y_POS = y
        # self.star_rect = rect
        self.X_POS = x * math.cos(self.angle) + 300
        self.Y_POS = y * math.sin(self.angle) + 300
        self.angle += 0.02
        return [self.X_POS, self.Y_POS]
