import pygame
import Maths

class Collided():
    DOWN = 1
    UP = 2
    LEFT = 3
    RIGHT = 4

class Collision():
    def __init__(self,entity,level):
        self.entity = entity
        self.level = level
        self.result = []

    def checkX(self):
        #check if left border is reached 
        self.xCollided = False
        if(self.entity.pos.x < 0):
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
            return
        #RIGHT
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x)+1].colliding):
            if(self.entity.vel.x > 0):
                self.entity.vel.x = 0
                self.entity.pos.x = int(self.entity.pos.x)
        #LEFT
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x)].colliding): 
            if(self.entity.vel.x < 0):
                self.entity.vel.x = 0
                self.entity.pos.x = int(self.entity.pos.x)+1

    def checkY(self):
        #   a----b
        #   |    | 
        #   c----d
        #DOWN C
        if(self.level[int(self.entity.pos.y+1)][int(self.entity.pos.x+0.05)].colliding):
            if(self.entity.vel.y > 0):
                self.entity.vel.y = 0
                self.entity.pos.y = int(self.entity.pos.y)
                self.entity.traits['jumpTrait'].maxReached = False
                self.entity.traits['jumpTrait'].timer = 0
        #UP A
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x+0.05)].colliding):
            if(self.entity.vel.y < 0):
                self.entity.vel.y = 0
                self.entity.pos.y = int(self.entity.pos.y)+1
        #DOWN D
        if(self.level[int(self.entity.pos.y)+1][int(self.entity.pos.x-0.05)+1].colliding):
            if(self.entity.vel.y > 0):
                self.entity.vel.y = 0
                self.entity.pos.y = int(self.entity.pos.y)
                self.entity.traits['jumpTrait'].maxReached = False
                self.entity.traits['jumpTrait'].timer = 0
        #UP B
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x-0.05)+1].colliding):
            if(self.entity.vel.y < 0):
                self.entity.vel.y = 0
                self.entity.pos.y = int(self.entity.pos.y)+1

    def checkCollision(self):
        try:
            self.checkX()
            self.checkY()
        except IndexError:
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
            self.checkY()


        
