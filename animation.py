import pygame

class animation():
    def __init__(self,images):
        self.images = images
        self.timer = 0
        self.index = 0
        self.image = self.images[self.index]

    def update(self,condition=True):
        self.timer += 1
        if(self.timer % 100 == 0):
            if(self.index < len(self.images)-1):
                self.index+=1   
            else:
                self.index = 0
        self.image = self.images[self.index]


