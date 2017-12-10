import pygame

class Animation():
    def __init__(self,images,idleSprite=None,airSprite=None):
        self.images = images
        self.timer = 0
        self.index = 0
        self.image = self.images[self.index]
        self.idleSprite = idleSprite
        self.airSprite = airSprite

    def update(self):
        self.timer += 1
        if(self.timer % 10 == 0):
            if(self.index < len(self.images)-1):
                self.index+=1   
            else:
                self.index = 0
        self.image = self.images[self.index]

    def idle(self):
        self.image = self.idleSprite
    
    def inAir(self):
        self.image = self.airSprite

