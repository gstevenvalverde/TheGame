import pygame

import BoyBuilder

import CommandUpdate
import CommandDraw
import CommandUp
import CommandDown
import CommandLeft
import CommandRight
import CommandUpLeft
import CommandUpRight
import CommandDownLeft
import CommandDownRight
import Context
import Director
import MoveCircularStrategy

import Play
import StarBuilder


class Game:
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self):

        self.boyBuilder = BoyBuilder.BoyBuilder()
        self.starBuilder = StarBuilder.StarBuilder()
        self.director = Director.Director()
        self.SCREEN.fill((255, 255, 255))
        self.stars = []

        self.director.make_level_1(self.boyBuilder, 100, 650, self.SCREEN)
        self.player = self.boyBuilder.get_result()

        self.make_stars()

        self.CommandUpdate = CommandUpdate.CommandUpdate(self.player)
        self.CommandDraw = CommandDraw.CommandDraw(self.player)
        self.CommandUp = CommandUp.CommandUp(self.player)
        self.CommandDown = CommandDown.CommandDown(self.player)
        self.CommandLeft = CommandLeft.CommandLeft(self.player)
        self.CommandRight = CommandRight.CommandRight(self.player)
        self.CommandDownLeft = CommandDownLeft.CommandDownLeft(self.player)
        self.CommandDownRight = CommandDownRight.CommandDownRight(self.player)
        self.CommandUpLeft = CommandUpLeft.CommandUpLeft(self.player)
        self.CommandUpRight = CommandUpRight.CommandUpRight(self.player)

        self.play = Play.Play()

        self.context = Context.Context()
        self.set_strategy()

    def main(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()

        while run:

            for event in pygame.event.get():
                self.play.set_command(self.CommandUpdate)
                if event.type == pygame.QUIT:
                    run = False
                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_w]:
                    self.play.set_command(self.CommandUp)
                elif user_input[pygame.K_s]:
                    self.play.set_command(self.CommandDown)
                elif user_input[pygame.K_a]:
                    self.play.set_command(self.CommandLeft)
                elif user_input[pygame.K_d]:
                    self.play.set_command(self.CommandRight)
                elif user_input[pygame.K_q]:
                    self.play.set_command(self.CommandUpLeft)
                elif user_input[pygame.K_e]:
                    self.play.set_command(self.CommandUpRight)
                elif user_input[pygame.K_z]:
                    self.play.set_command(self.CommandDownLeft)
                elif user_input[pygame.K_c]:
                    self.play.set_command(self.CommandDownRight)

            self.collitions()
            self.SCREEN.fill((255, 255, 255))
            self.play.set_command(self.CommandDraw)
            # self.set_strategy()
            self.move_stars()
            self.draw_stars()
            clock.tick(30)
            pygame.display.update()

    def collitions(self):
        for star in self.stars:
            if star.star_rect.colliderect(self.player.boy_rect):
                print("colision")
                self.stars.remove(star)

    def make_stars(self):
        self.director.make_level_1(self.starBuilder, 300, 300, self.SCREEN)
        star = self.starBuilder.get_result()
        self.stars.append(star)

        self.director.make_level_1(self.starBuilder, 100, 100, self.SCREEN)
        star = self.starBuilder.get_result()
        self.stars.append(star)

        self.director.make_level_1(self.starBuilder, 500, 100, self.SCREEN)
        star = self.starBuilder.get_result()
        self.stars.append(star)

    def draw_stars(self):
        for star in self.stars:
            star.draw()

    def set_strategy(self):
        self.context.set_strategy(MoveCircularStrategy.MoveCircularStrategy())

    def move_stars(self):
        for star in self.stars:
            position = self.context.execute_strategy(star.X_POS, star.Y_POS, star.star_rect)
            star.move_to(position[0], position[1])
