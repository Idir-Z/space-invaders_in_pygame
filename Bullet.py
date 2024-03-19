import pygame
from pygame.sprite import Sprite
class bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midbottom = game.ship.rect.midtop
        self.yPos = float(self.rect.y)
        self.groupe = game.bullets

    def update(self):
        if self.yPos < 0: #bullet is out of scope so needs to be removed from its groupe
            self.groupe.remove(self)
        else:
            self.yPos -= self.settings.bullet_speed
            self.rect.y = self.yPos
    def draw(self):
        pygame.draw.rect(self.screen , self.color, self.rect)