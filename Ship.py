import pygame
from math import floor
class ship:
    SPEED =1.2
    STEP = 1.3 # how many pixels the ship traverses each time also controled by the speed
    def __init__(self, ai_game):
        self.screen_space = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images\space_ship.png")
        self.rect = self.image.get_rect()
        self.center_ship()

        self.xPos= self.rect.centerx

        self.moving_left = False
        self.moving_right = False

    def update_position(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.xPos += ship.SPEED*ship.STEP
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.xPos -= ship.SPEED*ship.STEP
        self.rect.centerx = floor(self.xPos)
       
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.xPos= self.rect.centerx
        print("centered")

    def blitme(self):
        self.screen_space.blit(self.image, self.rect)