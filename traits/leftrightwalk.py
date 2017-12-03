import Maths 
from Collission_Detection import Collision
import random

class LeftRightWalkTrait():
    def __init__(self,entity,level):
        self.direction = 1 if random.randint(0,1) == 1 else -1
        self.entity = entity
        self.collDetection = Collision(self.entity,level)
        self.speed = 0.025
        self.entity.vel.x = 0.025 * self.direction

    def update(self):
        if(self.entity.vel.x == 0):
            self.direction *= -1
            self.entity.vel.x = self.speed * self.direction
        self.moveEntity()
        self.collDetection.checkCollision()

    def moveEntity(self):
        self.entity.pos.x += self.entity.vel.x
        self.entity.pos.y += self.entity.vel.y


        
        