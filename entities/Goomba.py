from classes.Sprites import Sprites
from classes.Animation import Animation
import classes.Maths
from traits.leftrightwalk import LeftRightWalkTrait
from entities.EntityBase import EntityBase
import pygame

class Goomba(EntityBase):
    def __init__(self,screen,spriteColl,x,y,level):
        super(Goomba,self).__init__(y,x-1,1.25)
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("goomba-1").image,
                                    self.spriteCollection.get("goomba-2").image])
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self,level)

    def update(self,camera):
        self.applyGravity()
        self.screen.blit(self.animation.image,(self.rect.x+camera.pos.x*32,self.rect.y))
        self.animation.update()
        self.leftrightTrait.update()
        
