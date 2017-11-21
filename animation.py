import pygame

class Animation():
    def __init__(self,images,idleSprite=None):
        self.images = images
        self.timer = 0
        self.index = 0
        self.image = self.images[self.index]
        self.idleSprite = idleSprite

    def update(self):
        self.timer += 1
        if(self.timer % 15 == 0):
            if(self.index < len(self.images)-1):
                self.index+=1   
            else:
                self.index = 0
        self.image = self.images[self.index]

    def idle(self):
        self.image = self.idleSprite

