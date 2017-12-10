from classes.Sprites import Sprites
from classes.Animation import Animation
import classes.Maths
import pygame
from traits.leftrightwalk import LeftRightWalkTrait
from entities.EntityBase import EntityBase

class Koopa(EntityBase):
    def __init__(self,screen,spriteColl,x,y,level):
        super(Koopa,self).__init__(y-1,x,1.25)
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("koopa-1").image,
                                    self.spriteCollection.get("koopa-2").image])
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self,level)
        self.timer = 0
        self.timeAfterDeath = 25

    def update(self,camera):
        if(self.alive):
            self.applyGravity()
            self.drawKoopa(camera)
            self.animation.update()
            self.leftrightTrait.update()
        else:
            if(self.timer < self.timeAfterDeath):
                self.screen.blit(self.spriteCollection.get("koopa-hiding").image,(self.rect.x+camera.pos.x*32,self.rect.y-32))
            else:
                self.alive = None
            self.timer+=0.1

    def drawKoopa(self,camera):
        if self.leftrightTrait.direction == -1:
            self.screen.blit(self.animation.image,(self.rect.x+camera.pos.x*32,self.rect.y-32))
        else:
            self.screen.blit(pygame.transform.flip(self.animation.image,True,False),(self.rect.x+camera.pos.x*32,self.rect.y-32))
    