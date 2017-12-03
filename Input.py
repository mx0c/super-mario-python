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
        if(keys[K_LEFT] and not keys[K_RIGHT]):
            self.entity.traits['goTrait'].direction = -1
        elif(keys[K_RIGHT] and not keys[K_LEFT]):
            self.entity.traits['goTrait'].direction =  1
        else:
            self.entity.traits['goTrait'].direction =  0
        if(keys[K_SPACE]):
            self.entity.traits['jumpTrait'].start()
        else:
            self.entity.applyGravity()
        if(keys[K_LSHIFT]):
            self.entity.traits['goTrait'].boost = True
        else:
            self.entity.traits['goTrait'].boost = False

        mouseX = pygame.mouse.get_pos()[0]/32
        mouseY = pygame.mouse.get_pos()[1]/32
        if pygame.mouse.get_pressed()[2]:
            self.entity.levelObj.addKoopa(mouseY,mouseX-self.entity.camera.pos.x)
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
            


    