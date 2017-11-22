from Sprites import Sprites
import pygame

class Level():
    def __init__(self,screen):
        self.sprites = Sprites()
        self.screen = screen
        self.getLineOfSprites = lambda x: [(self.sprites.backgroundSprites.get(x)) for i in range(20)]
        self.level = [
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("ground"),
                    self.getLineOfSprites("ground")
                ]
        self.addCloudSprite(5,5)
        self.addCloudSprite(13,3)
        self.addPipeSprite(8,10,4)
        self.addPipeSprite(12,12,4)
        self.addBushSprite(2,12)
        self.addBushSprite(17,12)
        self.addRandomBox(4,9)
    
    def drawLevel(self):
        for x in range(0,20):
            for y in range(0,15):
                dimensions = (x*32,y*32)
                if self.level[y][x].redrawBackground:
                    self.screen.blit(self.sprites.backgroundSprites.get("sky").image,dimensions)
                self.level[y][x].drawSprite(x,y,self.screen)

    def addCloudSprite(self,x,y):
        try:
            for yOff in range(0,2):
                for xOff in range(0,3):
                    self.level[y+yOff][x+xOff] = self.sprites.backgroundSprites.get("cloud{}_{}".format(yOff+1,xOff+1))
        except IndexError:
            return

    def addPipeSprite(self,x,y,length=2):
        try:
            #add Pipe Head
            self.level[y][x] = self.sprites.backgroundSprites.get("pipeL")
            self.level[y][x+1] = self.sprites.backgroundSprites.get("pipeR")
            #add pipe Body
            for i in range(1,length+20):
                self.level[y+i][x] = self.sprites.backgroundSprites.get("pipe2L")
                self.level[y+i][x+1] = self.sprites.backgroundSprites.get("pipe2R")
        except IndexError:
            return
    
    def addBushSprite(self,x,y):
        try:
            self.level[y][x] = self.sprites.backgroundSprites.get("bush_1")
            self.level[y][x+1] = self.sprites.backgroundSprites.get("bush_2")
            self.level[y][x+2] = self.sprites.backgroundSprites.get("bush_3")
        except IndexError:
            return
    
    def addRandomBox(self,x,y):
        try:
            self.level[y][x] = self.sprites.animations.get("randomBox")
        except IndexError:
            return