import Maths 
from Collission_Detection import Collision

class LeftRightWalkTrait():
    def __init__(self,entity,level,x,y):
        self.vel = Maths.vec2D(0.025,0)
        self.direction = 1
        self.entity = entity
        self.collDetection = Collision(self,level)
        self.pos = Maths.vec2D(y,x)

    def update(self):
        self.collDetection.checkX()
        if(self.vel.x == 0):
            self.direction *= -1
            self.vel.x = 0.025
        self.pos.x += self.vel.x * self.direction


        
        