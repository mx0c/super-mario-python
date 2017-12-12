import pygame
import classes.Maths
from classes.Tile import Tile

class Collider():
    def __init__(self,entity,level):
        self.entity = entity
        self.level = level
        self.result = []

    def checkX(self):
        #check for left level border
        if(self.entity.rect.x < 0):
            self.entity.rect.x = 0
            return
        #check for right level border
        if(self.entity.rect.x/32.0 > 59):
            self.entity.rect.x = 59*32
            return

        for row in self.level:
            for tile in row:
                #Only check if theres a collision Rectangle
                if(tile.rect is not None):
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.x > 0:
                            self.entity.rect.right = tile.rect.left
                            self.entity.vel.x = 0
                        if self.entity.vel.x < 0:
                            self.entity.rect.left = tile.rect.right
                            self.entity.vel.x = 0

    def checkY(self):
        for row in self.level:
            for tile in row:
                #Only check if theres a collision Rectangle
                if(tile.rect is not None):
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.y > 0:
                            self.entity.rect.bottom = tile.rect.top
                            self.entity.vel.y = 0
                            try:
                                self.entity.traits["jumpTrait"].reset()
                            except:
                                pass
                        if self.entity.vel.y < 0:
                            self.entity.rect.top = tile.rect.bottom
                            self.entity.vel.y = 0

