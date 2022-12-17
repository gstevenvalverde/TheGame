import math
import os
import pygame


class Star:

    def __init__(self, x, y, screen):
        self.X_POS = x
        self.Y_POS = y
        self.SCREEN = screen

        self.image = pygame.image.load(os.path.join("star", "star_rose.png"))
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.star_rect = self.image.get_rect()
        self.star_rect.x = self.X_POS
        self.star_rect.y = self.Y_POS

    def move_to(self, x, y):
        self.star_rect.x = x
        self.star_rect.y = y

    def draw(self):
        self.SCREEN.blit(self.image, (self.star_rect.x, self.star_rect.y))
