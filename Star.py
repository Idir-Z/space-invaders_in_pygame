
import pygame
from pygame.sprite import Sprite
from random import random
class star(Sprite):
    def __init__(self , game):
        super().__init__()
        self.screen= game.screen
        self.img = pygame.image.load("images\\star.png")
        self.rect = self.img.get_rect()
        self.img1 = pygame.image.load("images\\small_star.png")
        self.rect1 = self.img1.get_rect()

    def draw(self):
        #determin = random()
        #if determin < 0.5:
            self.screen.blit(self.img, self.rect)
        #else:
            #self.screen.blit(self.img1, self.rect1)