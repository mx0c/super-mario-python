import pygame
import Maths

class Collided():
    DOWN = 1
    UP = 2
    LEFT = 3
    RIGHT = 4

class Collision():
    def __init__(self,entity,level,debug=False):
        self.entity = entity
        self.level = level
        self.result = []
        self.debug = debug

    def checkX(self):
        #check if left border is reached 
        if(self.entity.pos.x < 0):
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
            return
        #RIGHT
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x)+1].colliding and self.entity.vel.x > 0):
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
        if(self.level[int(self.entity.pos.y)+1][int(self.entity.pos.x)+1].colliding and self.entity.vel.x > 0 and self.entity.vel.y < 0):
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
        #LEFT
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x)].colliding and self.entity.vel.x < 0): 
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)+1
        if(self.level[int(self.entity.pos.y+1)][int(self.entity.pos.x)].colliding and self.entity.vel.x < 0 and self.entity.vel.y < 0):
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)+1
       

    def checkY(self):
        #   a----b
        #   |    | 
        #   c----d
        #DOWN C
        if(self.level[int(self.entity.pos.y+1)][int(self.entity.pos.x+0.05)].colliding and self.entity.vel.y > 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)
            if hasattr(self.entity, 'traits'):
                self.entity.traits['jumpTrait'].reset()
        #UP A
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x+0.05)].colliding and self.entity.vel.y < 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)+1

        #DOWN D
        if(self.level[int(self.entity.pos.y)+1][int(self.entity.pos.x-0.05)+1].colliding and self.entity.vel.y > 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)
            if hasattr(self.entity, 'traits'):
                self.entity.traits['jumpTrait'].reset()
        #UP B
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x-0.05)+1].colliding and self.entity.vel.y < 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)+1

    def checkCollision(self):
        try:            
            self.checkY()
            self.checkX()
        except IndexError:
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
            self.checkY()


        
