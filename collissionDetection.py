import pygame
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

    def checkCollision(self):
        #   a----b
        #   |    | 
        #   c----d
        self.mario.pos.y += self.mario.vel.y
        self.mario.pos.x += self.mario.vel.x
        
        erg = []
        a = self.level[int(self.mario.pos.y)][int(self.mario.pos.x)]
        b = self.level[int(self.mario.pos.y)][int(self.mario.pos.x+1)]
        c = self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x)]
        d = self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x+1)]

        self.mario.pos.x -= self.mario.vel.x
        self.mario.pos.y -= self.mario.vel.y
        
        #check for intersection
        if(c or d):
            erg.append(collided.DOWN)
        if(a or b):
            erg.append(collided.UP)
        if(a or c):
            erg.append(collided.LEFT)
        if(b or d):
            erg.append(collided.RIGHT)
        
        if(not erg):
            return [False]
        else:
            return erg
