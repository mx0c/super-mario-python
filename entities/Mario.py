from classes.Sprites import Sprites
import pygame
from pygame.locals import *
import classes.Maths
from traits import go,jump
from traits.go import goTrait
from traits.jump import jumpTrait
from classes.Animation import Animation
from classes.Collider import Collider
from classes.Camera import Camera
from entities.EntityBase import EntityBase
from classes.EntityCollider import EntityCollider

class Mario(EntityBase):
    def __init__(self,x,y,level,screen,gravity=1.25):
        super(Mario,self).__init__(x,y,gravity)
        self.spriteCollection = Sprites().spriteCollection
        self.camera = Camera(self.rect)
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
        self.collision = Collider(self,self.level)
        self.screen = screen
        self.EntityCollider = EntityCollider(self)

    def drawMario(self):
        self.updateTraits()
        self.moveMario()

    def moveMario(self):
        self.rect.y += self.vel.y
        self.collision.checkY()
        self.rect.x += self.vel.x
        self.collision.checkX()
        #Camera Offset + Camera Move
        if self.rect.x/32.0 > 10 and self.rect.x/32.0 < 50:
            self.camera.pos.x = -self.rect.x/32.0+10

    def checkEntityCollision(self):
        for ent in self.levelObj.entityList:
            if self.EntityCollider.check(ent):
                return False
        return True