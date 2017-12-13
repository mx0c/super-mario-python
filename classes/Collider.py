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
            self.entity.vel.x = 0
            return
        #check for right level border
        if(self.entity.rect.x/32.0 > 59):
            self.entity.rect.x = 59*32
            self.entity.vel.x = 0
            return

        rows = [self.level[self.entity.getPosIndex().y],self.level[self.entity.getPosIndex().y+1]]
        for row in rows:
            tiles = row[self.entity.getPosIndex().x:self.entity.getPosIndex().x+2]
            for tile in tiles:
                if(tile.rect is not None):
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.x > 0:
                            self.entity.rect.right = tile.rect.left
                            self.entity.vel.x = 0
                        if self.entity.vel.x < 0:
                            self.entity.rect.left = tile.rect.right
                            self.entity.vel.x = 0

    def checkY(self):
        rows = [self.level[self.entity.getPosIndex().y],self.level[self.entity.getPosIndex().y+1]]
        for row in rows:
            tiles = row[self.entity.getPosIndex().x:self.entity.getPosIndex().x+2]
            for tile in tiles:
                if(tile.rect is not None):
                    if self.entity.rect.colliderect(tile.rect):
                        if self.entity.vel.y > 0:
                            self.entity.rect.bottom = tile.rect.top
                            self.entity.vel.y = 0
                            #TODO: Refactor
                            try:
                                self.entity.traits["jumpTrait"].reset()
                            except Exception:
                                pass
                        if self.entity.vel.y < 0:
                            self.entity.rect.top = tile.rect.bottom
                            self.entity.vel.y = 0

