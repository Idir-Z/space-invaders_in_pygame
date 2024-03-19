import pygame
from pygame.sprite import Sprite

class alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load("images\\alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    def draw(self):
        self.screen.blit(self.image, self.rect)