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
    def __init__(self,x,y,level,screen,gravity=0.7):
        self.pos = maths.vec2D(x,y)
        self.vel = maths.vec2D()
        self.gravity = gravity
        self.spritesObj = sprites()
        self.jumpTrait = jumpTrait()
        self.animation = animation([self.spritesObj.mario_run1,self.spritesObj.mario_run2,self.spritesObj.mario_run3],self.spritesObj.mario_idle)
        self.goTrait = goTrait(self.animation,screen)
        self.collision = Collision(self,level)

    def applyGravity(self):
        self.vel.y = self.gravity

    def drawMario(self):
        self.collision.checkCollision()
        self.goTrait.update(self)

    def moveMario(self):
        self.pos.y += self.vel.y
        self.pos.x += self.vel.x
        