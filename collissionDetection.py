class collided():
    DOWN = 1
    UP = 2
    LEFT = 3
    RIGHT = 4


class Collision():
    def __init__(self,mario,level):
        self.mario = mario
        self.level = level

    
    def checkCollision(self):
        try:
            if(self.mario.pos.x < 0):
                raise(IndexError)
            #Collisiondetection for Blocks under Mario
            if(self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x)] or self.level[int(self.mario.pos.y+1)][int(self.mario.pos.x+1)]):
                return collided.DOWN
            else:
                return False
        except (IndexError):
            self.mario.pos.x = 11
            self.mario.pos.y = 11
