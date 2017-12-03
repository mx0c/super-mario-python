from Sprites import Sprites
from Animation import Animation
import Maths
import pygame
from traits.leftrightwalk import LeftRightWalkTrait
from entities.EntityBase import EntityBase

class Koopa(EntityBase):
    def __init__(self,screen,spriteColl,x,y,level):
        super(Koopa,self).__init__(y-1,x,0.04)
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("koopa-1").image,
                                    self.spriteCollection.get("koopa-2").image])
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self,level)

    def update(self,camera):
        self.applyGravity()
        self.drawKoopa(camera)
        self.animation.update()
        self.leftrightTrait.update()
    
    def drawKoopa(self,camera):
        if self.leftrightTrait.direction == -1:
            self.screen.blit(self.animation.image,((self.pos.x+camera.pos.x)*32,(self.pos.y-1)*32))
        else:
            self.screen.blit(pygame.transform.flip(self.animation.image,True,False),((self.pos.x+camera.pos.x)*32,(self.pos.y-1)*32))