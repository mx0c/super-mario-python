import sprites
import pygame
from pygame.locals import *

class mario():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = {"x":0,"y":0}
        self.maxVelY = 0.04
        self.maxVelX = 0.01
        self.marioSprite = sprites.sprites().mario
		
    def drawMario(self,screen):
        screen.blit(self.marioSprite,(self.x*32,self.y*32))
	
    def jump(self):
        if self.y > 11:
            self.vel["y"] = 0
        if self.vel["y"] > -self.maxVelY:
            self.vel["y"] -= 0.0002
            self.y += self.vel["y"]
        elif self.y < 11 :
            self.vel["y"] += 0.0002
            self.y += self.vel["y"]
    
    def sink(self):
        if self.y < 11:
            if self.vel["y"] < self.maxVelY:
                self.vel["y"] += 0.0002
            self.y += self.vel["y"]
        else:
            self.vel["y"] = 0

    def RunLeft(self):
        if self.vel["x"] > -self.maxVelX:
            self.vel["x"] -= 0.00005
            self.x += self.vel["x"]
        else:
            self.x += self.vel["x"]

    def RunRight(self):
        if self.vel["x"] < self.maxVelX:
            self.vel["x"] += 0.00005
            self.x += self.vel["x"]
        else:
            self.x += self.vel["x"]
   