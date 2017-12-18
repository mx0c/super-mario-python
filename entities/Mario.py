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
from sfx.Sound import Sound

class Mario(EntityBase):
    def __init__(self,x,y,level,screen,dashboard,gravity=1.25):
        super(Mario,self).__init__(x,y,gravity)
        self.spriteCollection = Sprites().spriteCollection
        self.camera = Camera(self.rect,self)
        self.sound = Sound()
        
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
        self.collision = Collider(self,level)
        self.screen = screen
        self.EntityCollider = EntityCollider(self)
        self.dashboard = dashboard
        self.restart = False

    def update(self):
        self.updateTraits()
        self.moveMario()
        self.camera.move()
        self.applyGravity()
        self.checkEntityCollision()

    def moveMario(self):
        self.rect.y += self.vel.y
        self.collision.checkY()
        self.rect.x += self.vel.x
        self.collision.checkX()

    def checkEntityCollision(self):
        for ent in self.levelObj.entityList:
            collission = self.EntityCollider.check(ent)
            if(collission != False):
                if(ent.type == "Item"):
                        self.levelObj.entityList.remove(ent)
                        self.dashboard.points += 100
                        self.dashboard.coins += 1
                        self.sound.play_sfx(self.sound.coin)
                elif(ent.type == "Block"):
                    if(not ent.triggered):
                        self.sound.play_sfx(self.sound.bump)
                    ent.triggered = True
                elif(ent.type == "Mob"):
                    if(collission == "top"):
                        self.sound.play_sfx(self.sound.bump)
                    if collission == "top" and (ent.alive == True or ent.alive == "shellBouncing"):
                        self.rect.bottom = ent.rect.top
                        self.bounce()
                        self.killEntity(ent)
                    elif collission == "top" and ent.alive == "sleeping":
                        self.rect.bottom = ent.rect.top
                        self.bounce()
                        ent.alive = False
                    elif collission and ent.alive == "sleeping":
                        if(ent.rect.x < self.rect.x):
                            ent.leftrightTrait.direction = -1
                        else:
                            ent.leftrightTrait.direction = 1
                        ent.alive = "shellBouncing"
                    elif collission and ent.alive == True:
                        self.gameOver()

    def bounce(self):
        self.traits['bounceTrait'].jump = True
        
    def killEntity(self,ent):
        if ent.__class__.__name__ != "Koopa":
            ent.alive = False
        else:
            ent.timer = 0
            ent.alive = "sleeping"
        self.dashboard.points += 100
                
    def gameOver(self):
        srf = pygame.Surface((640,480))
        srf.set_colorkey((255,255,255), pygame.RLEACCEL)
        
        for i in range(500,20,-3):
            srf.fill((0,0,0))
            pygame.draw.circle(srf,(255,255,255),(int(self.camera.pos.x*32+self.rect.x)+16,self.rect.y+16),i)
            self.screen.blit(srf,(0,0))
            pygame.display.update()
        self.restart = True

    def getPos(self):
        return (self.camera.pos.x*32+self.rect.x, self.rect.y)