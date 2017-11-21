import Spritesheet as Sprite
import pygame

class Sprite():
    def __init__(self,image,colliding,animation = None):
        self.image = image
        self.colliding = colliding 
        self.animation = animation 

    def drawSprite(self,x,y,screen):
        if(self.animation == None):
            screen.blit(self.image,(x*32,y*32))
        else:
            self.animation.update()
            screen.blit(self.animation.image,(x*32,y*32))
