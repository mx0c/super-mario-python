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
from traits.bounce import bounceTrait

class Mario(EntityBase):
    def __init__(self,x,y,level,screen,gravity=1.25):
        super(Mario,self).__init__(x,y,gravity)
        self.spriteCollection = Sprites().spriteCollection
        self.camera = Camera(self.rect)
        self.animation = Animation([self.spriteCollection["mario_run1"].image,
            self.spriteCollection["mario_run2"].image,
            self.spriteCollection["mario_run3"].image
        ],self.spriteCollection["mario_idle"].image,self.spriteCollection["mario_jump"].image)
        self.traits = {
            "jumpTrait":jumpTrait(self),
            "goTrait":goTrait(self.animation,screen,self.camera,self),
            "bounceTrait":bounceTrait(self)
        }
        self.levelObj = level
        self.collision = Collider(self,level.level)
        self.screen = screen
        self.EntityCollider = EntityCollider(self)
        self.points = 0
        self.restart = False

    def update(self):
        self.updateTraits()
        self.moveMario()
        self.applyGravity()

    def moveMario(self):
        self.rect.y += self.vel.y
        self.collision.checkY()
        self.rect.x += self.vel.x
        self.collision.checkX()
        #Camera Offset + Camera Move
        if self.rect.x/32.0 > 10 and self.rect.x/32.0 < 50:
            self.camera.pos.x = -self.rect.x/32.0+10
        self.checkEntityCollision()

    def checkEntityCollision(self):
        for ent in self.levelObj.entityList:
            collission = self.EntityCollider.check(ent)
            if(collission != False and ent.__class__.__name__ == "Coin"):
                self.levelObj.entityList.remove(ent)
                self.points += 100
            else:
                if collission == "top" and (ent.alive == True or ent.alive == "shellBouncing"):
                    self.rect.bottom = ent.rect.top
                    self.bounce()
                    self.killEntity(ent)
                elif collission == "top" and ent.alive == "sleeping":
                    self.rect.bottom = ent.rect.top
                    self.bounce()
                    ent.alive = False
                elif collission and ent.alive == "sleeping":
                    if(ent.rect.right < self.rect.left):
                        ent.leftrightTrait.direction = 1
                    else:
                        ent.leftrightTrait.direction = -1
                    ent.alive = "shellBouncing"
                elif collission and ent.alive == True:
                    #game over
                    self.restart = True

    def bounce(self):
        self.traits['bounceTrait'].jump = True
        
    def killEntity(self,ent):
        if ent.__class__.__name__ != "Koopa":
            ent.alive = False
        else:
            ent.timer = 0
            ent.alive = "sleeping"
        self.points += 100
                