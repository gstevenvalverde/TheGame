import os
import pygame


class Boy:

    def __init__(self, x, y, screen):
        self.X_POS = x
        self.Y_POS = y
        self.SCREEN = screen

        self.up_img = [pygame.image.load(os.path.join("player/up", "up1.png")),
                       pygame.image.load(os.path.join("player/up", "up2.png")),
                       pygame.image.load(os.path.join("player/up", "up3.png")),
                       pygame.image.load(os.path.join("player/up", "up4.png"))]

        self.down_img = [pygame.image.load(os.path.join("player/down", "down1.png")),
                         pygame.image.load(os.path.join("player/down", "down2.png")),
                         pygame.image.load(os.path.join("player/down", "down3.png")),
                         pygame.image.load(os.path.join("player/down", "down4.png"))]

        self.left_img = [pygame.image.load(os.path.join("player/left", "left1.png")),
                         pygame.image.load(os.path.join("player/left", "left2.png")),
                         pygame.image.load(os.path.join("player/left", "left3.png")),
                         pygame.image.load(os.path.join("player/left", "left4.png"))]

        self.right_img = [pygame.image.load(os.path.join("player/right", "right1.png")),
                          pygame.image.load(os.path.join("player/right", "right2.png")),
                          pygame.image.load(os.path.join("player/right", "right3.png")),
                          pygame.image.load(os.path.join("player/right", "right4.png"))]

        self.up_left_img = [pygame.image.load(os.path.join("player/up_left", "up_left1.png")),
                            pygame.image.load(os.path.join("player/up_left", "up_left2.png")),
                            pygame.image.load(os.path.join("player/up_left", "up_left3.png")),
                            pygame.image.load(os.path.join("player/up_left", "up_left4.png"))]

        self.up_right_img = [pygame.image.load(os.path.join("player/up_right", "up_right1.png")),
                             pygame.image.load(os.path.join("player/up_right", "up_right2.png")),
                             pygame.image.load(os.path.join("player/up_right", "up_right3.png")),
                             pygame.image.load(os.path.join("player/up_right", "up_right4.png"))]

        self.down_left_img = [pygame.image.load(os.path.join("player/down_left", "down_left1.png")),
                              pygame.image.load(os.path.join("player/down_left", "down_left2.png")),
                              pygame.image.load(os.path.join("player/down_left", "down_left3.png")),
                              pygame.image.load(os.path.join("player/down_left", "down_left4.png"))]

        self.down_right_img = [pygame.image.load(os.path.join("player/down_right", "down_right1.png")),
                               pygame.image.load(os.path.join("player/down_right", "down_right2.png")),
                               pygame.image.load(os.path.join("player/down_right", "down_right3.png")),
                               pygame.image.load(os.path.join("player/down_right", "down_right4.png"))]

        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False

        self.step_index = 0
        self.image = self.down_img[0]
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS

    def update(self):
        if self.step_index >= 16:
            self.step_index = 0

    def up(self):
        self.boy_up = True
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.up_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.Y_POS -= 3
        self.step_index += 1

    def down(self):
        self.boy_up = False
        self.boy_down = True
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.down_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.Y_POS += 3
        self.step_index += 1

    def left(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = True
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.left_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.X_POS -= 3
        self.step_index += 1

    def right(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = True
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.right_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.X_POS += 3
        self.step_index += 1

    def up_left(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = True
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.up_left_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.X_POS -= 3
        self.Y_POS -= 3
        self.step_index += 1

    def up_right(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = True
        self.boy_down_left = False
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.up_right_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.X_POS += 3
        self.Y_POS -= 3
        self.step_index += 1

    def down_left(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = True
        self.boy_down_right = False
        self.image = pygame.transform.scale(self.down_left_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.X_POS -= 3
        self.Y_POS += 3
        self.step_index += 1

    def down_right(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = True
        self.image = pygame.transform.scale(self.down_right_img[self.step_index // 4], (80, 80))
        self.boy_rect = self.image.get_rect()
        self.boy_rect.x = self.X_POS
        self.boy_rect.y = self.Y_POS
        self.X_POS += 3
        self.Y_POS += 3
        self.step_index += 1

    def stop(self):
        self.boy_up = False
        self.boy_down = False
        self.boy_left = False
        self.boy_right = False
        self.boy_up_left = False
        self.boy_up_right = False
        self.boy_down_left = False
        self.boy_down_right = False

    def draw(self):
        self.SCREEN.blit(self.image, (self.boy_rect.x, self.boy_rect.y))
        # if self.boy_rect.colliderect(wall):
        #     pygame.time.delay(1000)
        #     self.X_POS -= 3
        #     self.Y_POS -= 3
