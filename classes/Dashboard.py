from classes.Font import Font
import pygame

class Dashboard(Font):
    def __init__(self,filePath,size,screen):
        Font.__init__(self,filePath,size)
        self.screen = screen
        self.levelName = "1-1"
        self.points = 0
        self.coins = 0
        self.ticks = 0
        self.time = 0

    def update(self):
        self.drawText("MARIO",50,20,15)
        self.drawText(self.genPointsString(),50,37,15)

        self.drawText("@x{}".format(self.genCoinString()),225,37,15)

        self.drawText("WORLD",380,20,15)
        self.drawText(str(self.levelName),395,37,15)

        self.drawText("TIME",520,20,15)
        self.drawText(self.genTimeString(),535,37,15)

        #update Time
        self.ticks+=1
        if(self.ticks == 60):
            self.ticks = 0
            self.time += 1

    def drawText(self,text,x,y,size):
        for char in text:
            charSprite = pygame.transform.scale(self.charSprites[char],(size,size))
            self.screen.blit(charSprite,(x,y))
            x+=size+1

    def genCoinString(self):
        coinsString = ""
        zerosLeft = 2-len(str(self.coins))
        for i in range(0,zerosLeft):
            coinsString+="0"
        coinsString+=str(self.coins)
        return coinsString

    def genPointsString(self):
        pointsString = ""
        zerosLeft = 6-len(str(self.points))
        for i in range(0,zerosLeft):
            pointsString+="0"
        pointsString+=str(self.points)
        return pointsString

    def genTimeString(self):
        timeStr = ""
        zerosLeft = 3-len(str(self.time))
        for i in range(0,zerosLeft):
            timeStr+="0"
        timeStr+=str(self.time)
        return timeStr 