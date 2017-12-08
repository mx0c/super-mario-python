import pygame
import Maths
from Tile import Tile

class Collision():
    def __init__(self,entity,level):
        self.entity = entity
        self.level = level
        self.result = []

    def checkX(self):
        for row in self.level:
            for tile in row:
                #Only check if theres a collision Rectangle
                try:
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.x > 0:
                            self.entity.vel.x = 0
                            self.entity.rect.right = tile.rect.left
                        if self.entity.vel.x < 0:
                            self.entity.vel.x = 0
                            self.entity.rect.left = tile.rect.right
                except TypeError:
                    pass

    def checkY(self):
        for row in self.level:
            for tile in row:
                #Only check if theres a collision Rectangle
                try:
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.y > 0:
                            self.entity.rect.bottom = tile.rect.top
                            self.entity.vel.y = 0
                            self.entity.traits["jumpTrait"].reset()
                        if self.entity.vel.y < 0:
                            self.entity.rect.top = tile.rect.bottom
                            self.entity.vel.y = 0
                except TypeError:
                    pass
