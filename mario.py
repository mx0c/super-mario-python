from sprites import sprites
import pygame
from pygame.locals import *
import maths
from traits import go,jump
from traits.go import goTrait
from traits.jump import jumpTrait
from animation import animation
from collissionDetection import collided,Collision

class mario():
    def __init__(self,x,y,level,screen,gravity=0.04):
        self.pos = maths.vec2D(x,y)
        self.vel = maths.vec2D()
        self.gravity = gravity
        self.spritesObj = sprites()
        self.jumpTrait = jumpTrait()
        self.animation = animation([self.spritesObj.mario_run1,self.spritesObj.mario_run2,self.spritesObj.mario_run3],self.spritesObj.mario_idle)
        self.goTrait = goTrait(self.animation,screen)
        self.collision = Collision(self,level)

    def applyGravity(self):
        if(collided.DOWN not in self.collision.checkCollision() and self.vel.y < self.goTrait.maxVel):
            self.vel.y += self.gravity
        else:
            self.vel.y = 0
            self.jumpTrait.reset()

    def drawMario(self):
        self.goTrait.update(self)
        self.moveMario()

    def moveMario(self):
        colissions = self.collision.checkCollision()
        if(False not in colissions):
            if(collided.UP in colissions):
                if(self.vel.y > 0):
                    self.pos.x += self.vel.x
            if(collided.LEFT in colissions and collided.DOWN not in colissions and collided.UP not in colissions):
                if(self.vel.x < 0):
                    self.pos.y += self.vel.y
        else:
            self.pos.y += self.vel.y
            self.pos.x += self.vel.x
            