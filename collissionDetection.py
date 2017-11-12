import pygame
import maths

class collided():
    DOWN = 1
    UP = 2
    LEFT = 3
    RIGHT = 4

class Collision():
    def __init__(self,mario,level):
        self.mario = mario
        self.level = level
        self.result = []

    def checkX(self):
        #RIGHT
        if(self.level[int(self.mario.pos.y)][int(self.mario.pos.x)+1] != 0):
            if(self.mario.vel.x > 0):
                self.mario.vel.x = 0
                self.mario.pos.x = int(self.mario.pos.x)
        #LEFT
        if(self.level[int(self.mario.pos.y)][int(self.mario.pos.x)] != 0):   
            if(self.mario.vel.x < 0):
                self.mario.vel.x = 0
                self.mario.pos.x = int(self.mario.pos.x)+1

    def checkY(self):
        #   a----b
        #   |    | 
        #   c----d
        #DOWN C
        if(self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x+0.1)] != 0):
            if(self.mario.vel.y > 0):
                self.mario.vel.y = 0
                self.mario.pos.y = int(self.mario.pos.y)
                self.mario.jumpTrait.maxReached = False
                self.mario.jumpTrait.timer = 0
        #UP A
        if(self.level[int(self.mario.pos.y)][int(self.mario.pos.x+0.1)] != 0):
            if(self.mario.vel.y < 0):
                self.mario.vel.y = 0
                self.mario.pos.y = int(self.mario.pos.y)+1
        #DOWN D
        if(self.level[int(self.mario.pos.y)+1][int(self.mario.pos.x-0.1)+1] != 0):
            print(self.mario.pos.x,self.mario.pos.y)
            if(self.mario.vel.y > 0):
                self.mario.vel.y = 0
                self.mario.pos.y = int(self.mario.pos.y)
                self.mario.jumpTrait.maxReached = False
                self.mario.jumpTrait.timer = 0
        #UP B
        if(self.level[int(self.mario.pos.y)][int(self.mario.pos.x-0.1)+1] != 0):
            if(self.mario.vel.y < 0):
                self.mario.vel.y = 0
                self.mario.pos.y = int(self.mario.pos.y)+1
            
    def checkCollision(self):
        try:
            self.checkX()
            self.checkY()
        except IndexError:
            self.mario.pos = maths.vec2D(7,7)


        
