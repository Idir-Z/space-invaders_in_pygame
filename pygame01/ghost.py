import pygame,sys
from pygame.locals import *

class Ghost:
    def __init__( self,screen):
        self.im = pygame.image.load("ghost.png")
        self.rect = self.im.get_rect()
        self.rect.center = screen.get_rect().center
    def blitme(self,screen):
        screen.blit(self.im, self.rect)
