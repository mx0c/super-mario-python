import pygame
from pygame.locals import *
import sys
from random import randint
from classes.EntityCollider import EntityCollider

class Input():
    def __init__(self,entity):
        self.mouseX = 0
        self.mouseY = 0
        self.entity = entity

    def checkForInput(self):
        keys = pygame.key.get_pressed()
        if(keys[K_LEFT] and not keys[K_RIGHT]):
            self.entity.traits['goTrait'].direction = -1
        elif(keys[K_RIGHT] and not keys[K_LEFT]):
            self.entity.traits['goTrait'].direction =  1
        else:
            self.entity.traits['goTrait'].direction =  0
        if(keys[K_SPACE]):
            self.entity.traits['jumpTrait'].start()
        else:
            self.entity.gravity = 1.25
        if(keys[K_LSHIFT]):
            self.entity.traits['goTrait'].boost = True
        else:
            self.entity.traits['goTrait'].boost = False

        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[2]:
            self.entity.levelObj.addKoopa(mouseY/32,mouseX/32-self.entity.camera.pos.x)
            self.entity.levelObj.addGoomba(mouseY/32,mouseX/32-self.entity.camera.pos.x)
        if pygame.mouse.get_pressed()[0]:
            self.entity.levelObj.addCoin(mouseX/32-self.entity.camera.pos.x,mouseY/32)
            #self.entity.vel.x = 0
            #self.entity.vel.y = 0
            #self.entity.rect.x = mouseX-self.entity.camera.pos.x*32
            #self.entity.rect.y = mouseY
            #print(self.entity.getPosIndex().x,self.entity.getPosIndex().y)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F5:
                self.entity.restart = True
