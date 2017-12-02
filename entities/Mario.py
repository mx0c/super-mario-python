from Sprites import Sprites
import pygame
from pygame.locals import *
import Maths
from traits import go,jump
from traits.go import goTrait
from traits.jump import jumpTrait
from Animation import Animation
from Collission_Detection import Collided,Collision
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
        self.level = level
        self.collision = Collision(self,level,True)
        
    def drawMario(self):
        self.updateTraits(self.traits)
        self.moveMario()

    def debug(self):
        print(self.pos.x, self.pos.y, self.vel.x, self.vel.y)

    def moveMario(self):
        self.pos.y += self.vel.y
        self.pos.x += self.vel.x
        #Camera Offset + Camera Move
        if self.pos.x > 10 and self.pos.x < 50:
            self.camera.pos.x = -self.pos.x+10
        self.collision.checkCollision()