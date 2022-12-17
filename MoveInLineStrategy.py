import math
from abc import ABC

import IStrategy


class MoveInLineStrategy(IStrategy.IStrategy):

    def __init__(self):
        self.X_POS = 0
        self.Y_POS = 0
        self.rect = None

    def execute(self, x, y, rect):
        self.X_POS = x
        self.Y_POS = y + 5
        return [self.X_POS, self.Y_POS]
