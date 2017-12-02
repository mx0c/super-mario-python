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
        self.xCollided = False
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
        coll = []
        if(self.level[int(self.entity.pos.y+1)][int(self.entity.pos.x+0.05)].colliding and self.entity.vel.y > 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)
            self.entity.traits['jumpTrait'].maxReached = False
            self.entity.traits['jumpTrait'].timer = 0
            if(self.debug):
                coll.append("DOWN LEFT")
        #UP A
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x+0.05)].colliding and self.entity.vel.y < 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)+1
            if(self.debug):
                coll.append("UP LEFT")
        #DOWN D
        if(self.level[int(self.entity.pos.y)+1][int(self.entity.pos.x-0.05)+1].colliding and self.entity.vel.y > 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)
            self.entity.traits['jumpTrait'].maxReached = False
            self.entity.traits['jumpTrait'].timer = 0
            if(self.debug):
                coll.append("DOWN RIGHT")
        #UP B
        if(self.level[int(self.entity.pos.y)][int(self.entity.pos.x-0.05)+1].colliding and self.entity.vel.y < 0):
            self.entity.vel.y = 0
            self.entity.pos.y = int(self.entity.pos.y)+1
            if(self.debug):
                coll.append("DOWN RIGHT")
        print(coll)

    def checkCollision(self):
        try:
            self.checkX()
            self.checkY()
        except IndexError:
            self.entity.vel.x = 0
            self.entity.pos.x = int(self.entity.pos.x)
            self.checkY()


        
