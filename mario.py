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
        self.collision.debugRectangle(self.pos.x,self.pos.y,screen)
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
            if(collissionDetection.collided.DOWN in collisions):
                if(collissionDetection.collided.LEFT not in collisions and collissionDetection.collided.RIGHT not in collisions):
                    self.pos.x += self.vel.x
                if(self.vel.y >= 0):
                    self.vel.y = 0
                self.pos.y += self.vel.y
                self.jumpTrait.timer = 0
                self.jumpTrait.maxReached = False
            if(collissionDetection.collided.UP in collisions):
                if(collissionDetection.collided.LEFT not in collisions and collissionDetection.collided.RIGHT not in collisions):
                    self.pos.x += self.vel.x
                if(self.vel.y <= 0):
                    self.vel.y = 0
                self.pos.y += self.vel.y
            if(collissionDetection.collided.LEFT in collisions):
                self.pos.y += self.vel.y
                if(self.vel.x <= 0):
                    self.vel.x = 0
                self.pos.x += self.vel.x
            if(collissionDetection.collided.RIGHT in collisions):
                self.pos.y += self.vel.y
                if(self.vel.x >= 0):
                    self.vel.x = 0
                self.pos.x += self.vel.x   
        else:
            self.pos.y += self.vel.y
            self.pos.x += self.vel.x