from sprites import sprites
import pygame
from pygame.locals import *
class Editor():
    def __init__(self,level,screen):
        self.editorMode = False
        self.levelObj = level
        self.screen = screen
        self.sprites = sprites()

    def checkUserInput(self):

            if(self.editorMode):
                x = int(pygame.mouse.get_pos()[0]/32)
                y = int(pygame.mouse.get_pos()[1]/32)
                if pygame.mouse.get_pressed()[0]:
                    self.screen.blit(self.sprites.getSprite("sky").image,(x*32,y*32))
                if pygame.mouse.get_pressed()[2]:
                    self.screen.blit(self.sprites.getSprite("ground").image,(x*32,y*32))
      
                            
                    
            

