import Maths
from Collission_Detection import Collision
import random

class LeftRightWalkTrait():
    def __init__(self,entity,level):
        self.direction = 1 if random.randint(0,1) == 1 else -1
        self.entity = entity
        self.collDetection = Collision(self.entity,level)
        self.speed = 0.8
        self.entity.vel.x = self.speed * self.direction
        self.entity.rect.x += 1

    def update(self):
        if(self.entity.vel.x == 0):
            self.direction *= -1
            self.entity.vel.x = self.speed * self.direction
        self.moveEntity()

    def moveEntity(self):
        self.entity.rect.y += self.entity.vel.y
        self.collDetection.checkY()
        self.entity.rect.x += self.entity.vel.x
        self.collDetection.checkX()
