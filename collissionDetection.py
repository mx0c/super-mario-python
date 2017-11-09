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
        try:
            #   a----b
            #   |    | 
            #   c----d
            self.mario.moveMario()
            erg = []
            erg.append(self.level[int(self.mario.pos.y)][int(self.mario.pos.x)])
            erg.append(self.level[int(self.mario.pos.y)][int(self.mario.pos.x+1)])
            erg.append(self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x)])
            erg.append(self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x+1)])
            
            #check for intersection
            if(1 in erg):
                self.mario.pos.x -= self.mario.vel.x
                self.mario.pos.y -= self.mario.vel.y
                return True
            else:
                return False

        except (IndexError):
            self.mario.pos.x = 11
            self.mario.pos.y = 11
