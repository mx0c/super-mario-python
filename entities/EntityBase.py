from classes.Maths import vec2D
import pygame

class EntityBase(object):
    def __init__(self,x,y,gravity):
        self.vel = vec2D()
        self.rect = pygame.Rect(x*32,y*32,32,32)
        self.gravity = gravity
        self.traits = None
        self.alive = True
        self.timeAfterDeath = 5
        self.timer = 0
        self.type = ""

    def applyGravity(self):
         self.vel.y += self.gravity

    def updateTraits(self):
        for trait in self.traits.values():
            try:
                trait.update()
            except AttributeError:
                pass
    
    def getPosIndex(self,float=False):
        if(float):
            x = self.rect.x/32.0
            y = self.rect.y/32.0
        else:
            x = int(self.rect.x/32)
            y = int(self.rect.y/32)
        return vec2D(x,y)

