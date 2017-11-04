
class Collision():
    def __init__(self,mario,level):
        self.mario = mario
        self.level = level
    
    def checkCollision(self):
        if(self.level[round(self.mario.pos.y)][round(self.mario.pos.x)] or self.level[round(self.mario.pos.y)+1][round(self.mario.pos.x)] or self.level[round(self.mario.pos.y)+1][round(self.mario.pos.x)+1]):
            self.mario.vel.y = 0
