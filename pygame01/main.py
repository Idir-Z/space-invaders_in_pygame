import pygame,sys
from pygame.locals import *
from math import floor
from ghost import *
from pacman import *

pygame.init()
display = pygame.display.set_mode((400,400))
char = Pacman(display)

while True:
    display.fill((255,255,255))
    char.blitMe()
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        char.checkEvent(e)
    char.updatePos()
    pygame.time.delay(floor(1000/60))
        