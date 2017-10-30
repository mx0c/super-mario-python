import sprites
import pygame
from pygame.locals import *
import maths

class mario():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = maths.vec2D()
        self.maxVel = maths.vec2D(0.01,0.04)
        self.marioSprite = sprites.sprites().mario
        self.direction = 'R'
		
    def drawMario(self,screen):
        if(self.direction == 'R'):
            screen.blit(self.marioSprite ,(self.x*32,self.y*32))
        else:
            screen.blit(pygame.transform.flip(self.marioSprite,True,False),(self.x*32,self.y*32))
	
    def jump(self):
        if self.y > 11:
            self.vel.y = 0
        if self.vel.y > -self.maxVel.y:
            self.vel.y -= 0.0002
            self.y += self.vel.y
        elif self.y < 11 :
            self.vel.y += 0.0002
            self.y += self.vel.y
    
    def sink(self):
        if self.y < 11:
            if self.vel.y < self.maxVel.y:
                self.vel.y += 0.0002
            self.y += self.vel.y
        else:
            self.vel.y = 0

    def RunLeft(self):
        self.direction = 'L'
        if self.vel.x > -self.maxVel.x:
            self.vel.x -= 0.00005
            self.x += self.vel.x
        else:
            self.x += self.vel.x

    def RunRight(self):
        self.direction = 'R'
        if self.vel.x < self.maxVel.x:
            self.vel.x+= 0.00005
            self.x += self.vel.x
        else:
            self.x += self.vel.x
   