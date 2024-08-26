
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
        self.drop_speed = game.settings.alien_drop_speed
        self.speed = game.settings.alien_speed
        self.movement_direction=game.settings.fleet_direction #1 is right -1 left
        self.settings = game.settings
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.speed * self.settings.fleet_direction
        self.rect.x = self.x
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>= screen_rect.right or self.rect.left <=0:
            return True