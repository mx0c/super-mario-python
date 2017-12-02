import pygame
from pygame.locals import *
import sys

class Input():
    def __init__(self,entity):
        self.clicked = False
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True
                self.mouseX = pygame.mouse.get_pos()[0]/32
                self.mouseY = pygame.mouse.get_pos()[1]/32
            if event.type == pygame.MOUSEMOTION and self.clicked:
                self.mouseX = pygame.mouse.get_pos()[0]/32
                self.mouseY = pygame.mouse.get_pos()[1]/32
                self.entity.vel.x = 0
                self.entity.vel.y = 0       
                self.entity.pos.x = self.mouseX-self.entity.camera.pos.x
                self.entity.pos.y = self.mouseY 
            if event.type == pygame.MOUSEBUTTONUP:
                self.clicked = False


    