from entities.EntityBase import EntityBase
from classes.Animation import Animation
import pygame
from copy import copy

class RandomBox(EntityBase):
    def __init__(self,screen,spriteCollection,x,y,gravity = 0):
        super(RandomBox,self).__init__(x,y,gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = copy(self.spriteCollection.get('randomBox').animation)
        self.type = "Block"
        self.triggered = False
        self.time = 0
        self.maxTime = 10
        self.vel = 1

    def update(self,cam):
        if(self.alive and self.triggered == False):
            self.animation.update()
            self.screen.blit(self.spriteCollection.get("sky").image,(self.rect.x+cam.pos.x*32,self.rect.y))
            self.screen.blit(self.animation.image,(self.rect.x+cam.pos.x*32,self.rect.y-1))
        else:
            self.animation.image = self.spriteCollection.get("empty").image
            if(self.time < self.maxTime):
                self.time +=1
                self.rect.y -= self.vel
                self.screen.blit(self.spriteCollection.get("sky").image,(self.rect.x+cam.pos.x*32,self.rect.y+2))
                self.screen.blit(self.animation.image,(self.rect.x+cam.pos.x*32,self.rect.y-1))
            else:
                if(self.time < self.maxTime*2):
                    self.time+=1
                    self.rect.y += self.vel
                    self.screen.blit(self.spriteCollection.get("sky").image,(self.rect.x+cam.pos.x*32,self.rect.y+2))
                    self.screen.blit(self.animation.image,(self.rect.x+cam.pos.x*32,self.rect.y-1))
                else:
                    self.screen.blit(self.spriteCollection.get("sky").image,(self.rect.x+cam.pos.x*32,self.rect.y))
                    self.screen.blit(self.animation.image,(self.rect.x+cam.pos.x*32,self.rect.y-1))