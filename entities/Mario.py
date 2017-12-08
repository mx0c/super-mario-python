from Sprites import Sprites
import pygame
from pygame.locals import *
import Maths
from traits import go,jump
from traits.go import goTrait
from traits.jump import jumpTrait
from Animation import Animation
from Collission_Detection import Collision
from Camera import Camera
from entities.EntityBase import EntityBase

class Mario(EntityBase):
    def __init__(self,x,y,level,screen,gravity=0.04):
        super(Mario,self).__init__(x,y,gravity)
        self.spriteCollection = Sprites().spriteCollection
        self.camera = Camera(self.pos)
        self.animation = Animation([
            self.spriteCollection["mario_run1"].image,
            self.spriteCollection["mario_run2"].image,
            self.spriteCollection["mario_run3"].image
        ],self.spriteCollection["mario_idle"].image)
        self.traits = {
            "jumpTrait":jumpTrait(self),
            "goTrait":goTrait(self.animation,screen,self.camera,self)
        }
        self.level = level.level
        self.levelObj = level
        self.collision = Collision(self,self.level,True)
        self.screen = screen
        
    def drawMario(self):
        self.updateTraits()
        self.moveMario()

    def debug(self):
        print(self.pos.x, self.pos.y, self.vel.x, self.vel.y,self.rect.x,self.rect.y)
        pygame.draw.rect(self.screen,pygame.Color(255,255,255),self.rect,1)

    def moveMario(self):
        self.debug()
        self.rect.y += self.vel.y*32
        self.rect.x += self.vel.x*32

        #Camera Offset + Camera Move
        if self.rect.x/32.0 > 10 and self.rect.x/32.0 < 50:
            self.camera.pos.x = -self.rect.x/32.0+10
        self.collision.checkCollision()