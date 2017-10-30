import sprites
import pygame
from pygame.locals import *
import maths
from traits import go,jump

class mario():
    def __init__(self,x,y):
        self.pos = maths.vec2D(x,y)
        self.vel = maths.vec2D()
        self.marioSprite = sprites.sprites().mario
        self.goTrait = go.goTrait()
        self.jumpTrait = jump.jumpTrait()
		
    def drawMario(self,screen):
        self.updateMario()
        self.goTrait.update(self)
        if(self.goTrait.heading == 1):
            screen.blit(self.marioSprite ,(self.pos.x*32,self.pos.y*32))
        elif(self.goTrait.heading == -1):
            screen.blit(pygame.transform.flip(self.marioSprite,True,False),(self.pos.x*32,self.pos.y*32))

    def updateMario(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y