import pygame,sys
from pygame.locals import *
from math import floor

class Pacman:
    SPEED = 1.0
    STEP = 2.0
    def __init__(self, screen):
        self.screen= screen
        self.screenRect = screen.get_rect()

        self.image = pygame.image.load("images\pacman.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = screen.get_rect().midbottom

        self.movingRight= False
        self.movingLeft= False
        self.movingUp= False
        self.movingDown= False

        self.xPos= self.rect.centerx
        self.yPos= self.rect.centery

    def blitMe(self):
        self.screen.blit(self.image, self.rect)

    def updatePos(self):
        if self.movingRight:
            if (self.rect.left <= self.screenRect.width):
                self.xPos += (Pacman.STEP)*(Pacman.SPEED)
            else:
                self.xPos= -(self.rect.width/2)
            
        if self.movingLeft:
            if (self.rect.right >= 0):
                self.xPos -= (Pacman.STEP)*(Pacman.SPEED)
            else:
                self.xPos= self.screenRect.width + (self.rect.width/2)
        if self.movingUp:
            if (self.rect.bottom >= 0):
                self.yPos -= (Pacman.STEP)*(Pacman.SPEED)
            else:
                self.yPos = self.screenRect.height
        if self.movingDown:
            if (self.rect.top <= self.screenRect.height):
                self.yPos += (Pacman.STEP)*(Pacman.SPEED)
            else:
                self.yPos = 0
        
        self.rect.centerx = floor(self.xPos)    
        self.rect.centery = floor(self.yPos)
    def checkEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movingLeft= True
            if event.key == pygame.K_RIGHT:
                self.movingRight= True
            if event.key == pygame.K_UP:
                self.movingUp= True
            if event.key == pygame.K_DOWN:
                self.movingDown= True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.movingLeft= False
            if event.key == pygame.K_RIGHT:
                self.movingRight= False
            if event.key == pygame.K_UP:
                self.movingUp= False
            if event.key == pygame.K_DOWN:
                self.movingDown= False





