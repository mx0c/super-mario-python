import pygame
import Maths
from Tile import Tile

class Collision():
    def __init__(self,entity,level,debug=False):
        self.entity = entity
        self.level = level
        self.result = []
        self.debug = debug

    def checkX(self):
        for row in self.level:
            for tile in row:
                try:
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.x > 0: 
                            self.entity.rect.right = tile.rect.left
                            self.entity.vel.x = 0
                        if self.entity.vel.x < 0: 
                            self.entity.rect.left = tile.rect.right
                            self.entity.vel.x = 0
                except TypeError:
                    pass
       
    def checkY(self):
        for row in self.level:
            for tile in row:
                try:
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.y > 0:
                            self.entity.rect.bottom = tile.rect.top
                            self.entity.vel.y = 0
                        if self.entity.vel.y < 0:
                            self.entity.rect.top = tile.rect.bottom
                            self.entity.vel.y = 0
                except TypeError:
                    pass

    def checkCollision(self):          
        self.checkY()
        self.checkX()
        

    


        
