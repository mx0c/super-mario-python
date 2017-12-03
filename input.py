import pygame
from pygame.locals import *
import sys

class Input():
    def __init__(self,entity):
        self.mouseX = 0
        self.mouseY = 0
        self.entity = entity
    
    def checkForInput(self):
        keys = pygame.key.get_pressed()
        if(keys[K_LEFT]):
            self.entity.traits['goTrait'].direction = -1
        if(keys[K_RIGHT]):
            self.entity.traits['goTrait'].direction =  1
        if(not(keys[K_LEFT] or keys[K_RIGHT])):
            self.entity.traits['goTrait'].direction =  0

        mouseX = pygame.mouse.get_pos()[0]/32
        mouseY = pygame.mouse.get_pos()[1]/32
        if pygame.mouse.get_pressed()[2]:
            self.entity.levelObj.addGoomba(mouseY,mouseX-self.entity.camera.pos.x)
        if pygame.mouse.get_pressed()[0]:
            self.entity.vel.x = 0
            self.entity.vel.y = 0       
            print(self.entity.pos.x,self.entity.pos.y)
            self.entity.pos.x = mouseX
            self.entity.pos.x = mouseX-self.entity.camera.pos.x
            self.entity.pos.y = mouseY 
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    self.entity.traits['goTrait'].boost = False
                if event.key == K_SPACE:
                    self.entity.traits['jumpTrait'].jump = False
            if event.type == KEYDOWN:
                if event.key == K_LSHIFT:
                    self.entity.traits['goTrait'].boost = True
                if event.key == K_SPACE:
                   self.entity.traits['jumpTrait'].jump = True
            


    