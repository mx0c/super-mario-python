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
        if(collissionDetection.collided.DOWN not in self.collision.checkCollision() or False):
            self.animation.image = self.spritesObj.mario_jump
        if(self.goTrait.heading == 1):
            screen.blit(self.animation.image ,(self.pos.x*32,self.pos.y*32))
        elif(self.goTrait.heading == -1):
            screen.blit(pygame.transform.flip(self.animation.image,True,False),(self.pos.x*32,self.pos.y*32))

    def updateMario(self):
        collisions = self.collision.checkCollision()
        if(False not in collisions):
            if(collissionDetection.collided.DOWN in collisions and self.vel.y >= 0):
                print("Collided DOWN")
                self.pos.x += self.vel.x
                self.vel.y = 0
                self.jumpTrait.timer = 0
                self.jumpTrait.maxReached = False
            else:
                self.pos.x += self.vel.x
                self.pos.y += self.vel.y
            if(collissionDetection.collided.UP in collisions):
                print("Collided DOWN")
                self.pos.x += self.vel.x
                self.vel.y = 0
                self.applyGravity()
                self.pos.y += self.vel.y
            if(collissionDetection.collided.LEFT in collisions):
                print("Collided LEFT")
                self.vel.x = 0
            if(collissionDetection.collided.RIGHT in collisions):
                print("Collided RIGHT")
                self.vel.x = 0
        else:
            self.pos.y += self.vel.y
            self.pos.x += self.vel.x