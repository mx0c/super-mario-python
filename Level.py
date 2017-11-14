from sprites import sprites
import pygame

class Level():
    def __init__(self):
        self.sprites = sprites()
        self.getLineOfSprites = lambda x: [(self.sprites.getSprite(x)) for i in range(20)]
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
    
    def drawLevel(self,screen):
        for x in range(0,20):
            for y in range(0,15):
                dimensions = (x*32,y*32)
                screen.blit(self.sprites.getSprite("sky").image,dimensions)
                screen.blit(self.level[y][x].image,dimensions)

    def addCloudSprite(self,x,y):
        try:
            for yOff in range(0,2):
                for xOff in range(0,3):
                    self.level[y+yOff][x+xOff] = self.sprites.getSprite("cloud{}_{}".format(yOff+1,xOff+1))
        except IndexError:
            return

    def addPipeSprite(self,x,y,length=2):
        #add Pipe Head
        self.level[y][x] = self.sprites.getSprite("pipeL")
        self.level[y][x+1] = self.sprites.getSprite("pipeR")
        #add pipe Body
        try:
            for i in range(1,length+1):
                self.level[y+i][x] = self.sprites.getSprite("pipe2L")
                self.level[y+i][x+1] = self.sprites.getSprite("pipe2R")
        except IndexError:
            return
    
    def addBushSprite(self,x,y):
        try:
            self.level[y][x] = self.sprites.getSprite("bush_1")
            self.level[y][x+1] = self.sprites.getSprite("bush_2")
            self.level[y][x+2] = self.sprites.getSprite("bush_3")
        except IndexError:
            return