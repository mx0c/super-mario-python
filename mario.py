import sprites
import pygame
from pygame.locals import *
import maths
from traits import go,jump
import animation
import collissionDetection

class mario():
    def __init__(self,x,y,level,gravity=0.0005):
        self.pos = maths.vec2D(x,y)
        self.vel = maths.vec2D()
        self.gravity = gravity
        self.spritesObj = sprites.sprites()
        self.goTrait = go.goTrait()
        self.jumpTrait = jump.jumpTrait()
        self.animation = animation.animation([self.spritesObj.mario_run1,self.spritesObj.mario_run2,self.spritesObj.mario_run3])
        self.collision = collissionDetection.Collision(self,level)

    def applyGravity(self):
        self.vel.y += self.gravity

    def drawMario(self,screen):
        self.updateMario()
        self.goTrait.update(self)
        if(self.goTrait.direction != 0):
            self.animation.update()
        else:
            self.animation.image = self.spritesObj.mario_idle
        if(not self.collision.checkCollision()):
            self.animation.image = self.spritesObj.mario_jump
        if(self.goTrait.heading == 1):
            screen.blit(self.animation.image ,(self.pos.x*32,self.pos.y*32))
        elif(self.goTrait.heading == -1):
            screen.blit(pygame.transform.flip(self.animation.image,True,False),(self.pos.x*32,self.pos.y*32))

    def updateMario(self):
        if(self.collision.checkCollision() == collissionDetection.collided.DOWN and self.vel.y > 0):
            self.pos.x += self.vel.x
            self.vel.y = 0
            self.jumpTrait.timer = 0
            self.jumpTrait.maxReached = False
        else:
            self.pos.y += self.vel.y
            self.pos.x += self.vel.x