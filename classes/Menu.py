import pygame
from classes.Dashboard import Dashboard
import sys
from classes.Spritesheet import Spritesheet
import json

class Menu():
    def __init__(self,screen,dashboard,level,sound):
        self.screen = screen
        self.sound = sound
        self.start = False
        self.inSettings = False
        self.state = 0
        self.level = level
        self.dashboard = dashboard
        self.spritesheet = Spritesheet("./img/title_screen.png")
        self.menu_banner = self.spritesheet.image_at(0,60,2,colorkey=[255,0,220],ignoreTileSize=True,xTileSize=180,yTileSize=88)
        self.menu_dot = self.spritesheet.image_at(0,150,2,colorkey=[255,0,220],ignoreTileSize=True)
        self.loadSettings("./settings.json")

    def update(self):
        self.dashboard.update()
        self.checkInput()
        self.drawMenuBackground()
        if(not self.inSettings):
            self.drawMenu()
        else:
            self.drawSettings()

    def drawDot(self):
        if(self.state == 0):
            self.screen.blit(self.menu_dot,(145,273))
        elif(self.state == 1):
            self.screen.blit(self.menu_dot,(145,313))
        elif(self.state == 2):
            self.screen.blit(self.menu_dot,(145,353))
    
    def loadSettings(self,url):
        with open(url) as jsonData:
            data = json.load(jsonData)
            if(data["sound"]):
                self.music = True
                self.sound.music_channel.play(self.sound.soundtrack)
            else:
                self.music = False
            if(data["sfx"]):
                self.sfx = True
                self.sound.allowSFX = True
            else:
                self.sound.allowSFX = False
                self.sfx = False
    
    def saveSettings(self,url):
        data = {}
        data["sound"] = self.music
        data["sfx"] = self.sfx
        with open(url, 'w') as outfile:  
            json.dump(data, outfile)

    def drawMenu(self):
        self.drawDot()
        self.dashboard.drawText("START THE GAME",180,280,24)
        self.dashboard.drawText("SETTINGS",180,320,24)
        self.dashboard.drawText("EXIT",180,360,24)

    def drawMenuBackground(self):
        for y in range(0,13):
            for x in range(0,20):
                self.screen.blit(self.level.sprites.spriteCollection.get("sky").image,(x*32,y*32))
        for y in range(13,15):
            for x in range(0,20):
                self.screen.blit(self.level.sprites.spriteCollection.get("ground").image,(x*32,y*32))
        self.screen.blit(self.menu_banner,(150,80))
        self.screen.blit(self.level.sprites.spriteCollection.get("mario_idle").image,(2*32,12*32))
        self.screen.blit(self.level.sprites.spriteCollection.get("bush_1").image,(14*32,12*32))
        self.screen.blit(self.level.sprites.spriteCollection.get("bush_2").image,(15*32,12*32))
        self.screen.blit(self.level.sprites.spriteCollection.get("bush_2").image,(16*32,12*32))
        self.screen.blit(self.level.sprites.spriteCollection.get("bush_2").image,(17*32,12*32))
        self.screen.blit(self.level.sprites.spriteCollection.get("bush_3").image,(18*32,12*32))
        #self.screen.blit(self.level.sprites.spriteCollection.get("goomba-1").image,(16*32,12*32))
        
    def drawSettings(self):        
        self.drawDot()
        self.dashboard.drawText("MUSIC",180,280,24)
        if(self.music):
            self.dashboard.drawText("ON",340,280,24)
        else:
            self.dashboard.drawText("OFF",340,280,24)
        self.dashboard.drawText("SFX",180,320,24)
        if(self.sfx):
            self.dashboard.drawText("ON",340,320,24)
        else:
            self.dashboard.drawText("OFF",340,320,24)
        self.dashboard.drawText("BACK",180,360,24)

    def checkInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE):
                    sys.exit()
                elif(event.key == pygame.K_UP):
                    if(self.state > 0):
                        self.state -= 1
                elif(event.key == pygame.K_DOWN):
                    if(self.state < 2):
                        self.state += 1 
                elif(event.key == pygame.K_RETURN):
                    if(not self.inSettings):
                        if(self.state == 0):
                            self.dashboard.state = "play"
                            self.dashboard.time = 0
                            self.start = True
                        elif(self.state == 1):
                            self.inSettings = True
                            self.state = 0
                        elif(self.state == 2):
                            pygame.quit()
                            sys.exit()
                    else:
                        if(self.state == 0):
                            if(self.music):
                                self.sound.music_channel.stop()
                                self.music = False
                            else:
                                self.sound.music_channel.play(self.sound.soundtrack)    
                                self.music = True
                            self.saveSettings("./settings.json")
                        elif(self.state == 1):
                            if(self.sfx):
                                self.sound.allowSFX = False
                                self.sfx = False
                            else:
                                self.sound.allowSFX = True
                                self.sfx = True
                            self.saveSettings("./settings.json")
                        elif(self.state == 2):
                            self.inSettings = False
        pygame.display.update()