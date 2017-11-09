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

    def debugRectangle(self,x,y,screen):
        dbgStr = ""
 
        if(collided.DOWN in self.result):
            dbgStr += "DOWN "
            newy=y+1
            pygame.draw.rect(screen,(255,0,0),(x*32,newy*32,32,32),2)
        if(collided.UP in self.result):
            dbgStr += "UP "
            newy=y-1
            pygame.draw.rect(screen,(255,0,0),(x*32,newy*32,32,32),2)
        if(collided.LEFT in self.result):
            dbgStr += "LEFT "
            newx=x-1
            pygame.draw.rect(screen,(255,0,0),(newx*32,y*32,32,32),2)
        if(collided.RIGHT in self.result):
            dbgStr += "RIGHT "
            newx=x+1
            pygame.draw.rect(screen,(255,0,0),(newx*32,y*32,32,32),2)
        #pygame.draw.circle(screen,(0,0,255),(int(x*32),int(y*32)),2)
        print(dbgStr)
        

    def checkCollision(self):
        try:
            self.result = []
            if(self.mario.pos.x < 0):
                raise(IndexError)
            #Collisiondetection for Blocks under Mario
            if(self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x)] or self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x+1)]):
                self.result.append(collided.DOWN)
            #Collisiondetection for Blocks above Mario
            if(self.level[int(self.mario.pos.y-1)][int(self.mario.pos.x)] or self.level[int(self.mario.pos.y-1)][int(self.mario.pos.x+1)]):
                self.result.append(collided.UP)
            #Collisiondetection for Blocks left of Mario
            if(self.level[int(self.mario.pos.y)][int(self.mario.pos.x-1)]):
                self.result.append(collided.LEFT)
            #Collisiondetection for Blocks right of Mario
            if(self.level[int(self.mario.pos.y)][int(self.mario.pos.x+1)]):
                self.result.append(collided.RIGHT)
            if(not self.result):
                return [False]
            else:
                return self.result
        except (IndexError):
            self.mario.pos.x = 11
            self.mario.pos.y = 11
