import Maths 
from Collission_Detection import Collision

class LeftRightWalkTrait():
    def __init__(self,entity,level):
        self.direction = 1
        self.entity = entity
        self.collDetection = Collision(self.entity,level)

    def update(self,):
        if(self.entity.vel.x == 0):
            self.direction *= -1
            self.entity.vel.x = 0.025
        self.moveEntity()
        self.collDetection.checkCollision()

    def moveEntity(self):
        self.entity.pos.x += self.entity.vel.x * self.direction
        self.entity.pos.y += self.entity.vel.y


        
        