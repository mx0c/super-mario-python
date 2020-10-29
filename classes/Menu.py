import json
import sys
import os
import pygame

from classes.Spritesheet import Spritesheet


class Menu:
    def __init__(self, screen, dashboard, level, sound):
        self.screen = screen
        self.sound = sound
        self.start = False
        self.inSettings = False
        self.state = 0
        self.level = level
        self.music = True
        self.sfx = True
        self.currSelectedLevel = 1
        self.levelNames = []
        self.inChoosingLevel = False
        self.dashboard = dashboard
        self.levelCount = 0
        self.spritesheet = Spritesheet("./img/title_screen.png")
        self.menu_banner = self.spritesheet.image_at(
            0,
            60,
            2,
            colorkey=[255, 0, 220],
            ignoreTileSize=True,
            xTileSize=180,
            yTileSize=88,
        )
        self.menu_dot = self.spritesheet.image_at(
            0, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )
        self.menu_dot2 = self.spritesheet.image_at(
            20, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )
        self.loadSettings("./settings.json")

    def update(self):
        self.checkInput()
        if self.inChoosingLevel:
            return

        self.drawMenuBackground()
        self.dashboard.update()

        if not self.inSettings:
            self.drawMenu()
        else:
            self.drawSettings()

    def drawDot(self):
        if self.state == 0:
            self.screen.blit(self.menu_dot, (145, 273))
            self.screen.blit(self.menu_dot2, (145, 313))
            self.screen.blit(self.menu_dot2, (145, 353))
        elif self.state == 1:
            self.screen.blit(self.menu_dot, (145, 313))
            self.screen.blit(self.menu_dot2, (145, 273))
            self.screen.blit(self.menu_dot2, (145, 353))
        elif self.state == 2:
            self.screen.blit(self.menu_dot, (145, 353))
            self.screen.blit(self.menu_dot2, (145, 273))
            self.screen.blit(self.menu_dot2, (145, 313))

    def loadSettings(self, url):
        try:
            with open(url) as jsonData:
                data = json.load(jsonData)
                if data["sound"]:
                    self.music = True
                    self.sound.music_channel.play(self.sound.soundtrack, loops=-1)
                else:
                    self.music = False
                if data["sfx"]:
                    self.sfx = True
                    self.sound.allowSFX = True
                else:
                    self.sound.allowSFX = False
                    self.sfx = False
        except (IOError, OSError):
            self.music = False
            self.sound.allowSFX = False
            self.sfx = False
            self.saveSettings("./settings.json")

    def saveSettings(self, url):
        data = {"sound": self.music, "sfx": self.sfx}
        with open(url, "w") as outfile:
            json.dump(data, outfile)

    def drawMenu(self):
        self.drawDot()
        self.dashboard.drawText("CHOOSE LEVEL", 180, 280, 24)
        self.dashboard.drawText("SETTINGS", 180, 320, 24)
        self.dashboard.drawText("EXIT", 180, 360, 24)

    def drawMenuBackground(self, withBanner=True):
        for y in range(0, 13):
            for x in range(0, 20):
                self.screen.blit(
                    self.level.sprites.spriteCollection.get("sky").image,
                    (x * 32, y * 32),
                )
        for y in range(13, 15):
            for x in range(0, 20):
                self.screen.blit(
                    self.level.sprites.spriteCollection.get("ground").image,
                    (x * 32, y * 32),
                )
        if withBanner:
            self.screen.blit(self.menu_banner, (150, 80))
        self.screen.blit(
            self.level.sprites.spriteCollection.get("mario_idle").image,
            (2 * 32, 12 * 32),
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_1").image, (14 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_2").image, (15 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_2").image, (16 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_2").image, (17 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_3").image, (18 * 32, 12 * 32)
        )
        self.screen.blit(self.level.sprites.spriteCollection.get("goomba-1").image, (18.5*32, 12*32))

    def drawSettings(self):
        self.drawDot()
        self.dashboard.drawText("MUSIC", 180, 280, 24)
        if self.music:
            self.dashboard.drawText("ON", 340, 280, 24)
        else:
            self.dashboard.drawText("OFF", 340, 280, 24)
        self.dashboard.drawText("SFX", 180, 320, 24)
        if self.sfx:
            self.dashboard.drawText("ON", 340, 320, 24)
        else:
            self.dashboard.drawText("OFF", 340, 320, 24)
        self.dashboard.drawText("BACK", 180, 360, 24)

    def chooseLevel(self):
        self.drawMenuBackground(False)
        self.inChoosingLevel = True
        self.levelNames = self.loadLevelNames()
        self.drawLevelChooser()

    def drawBorder(self, x, y, width, height, color, thickness):
        pygame.draw.rect(self.screen, color, (x, y, width, thickness))
        pygame.draw.rect(self.screen, color, (x, y+width, width, thickness))
        pygame.draw.rect(self.screen, color, (x, y, thickness, width))
        pygame.draw.rect(self.screen, color, (x+width, y, thickness, width+thickness))

    def drawLevelChooser(self):
        j = 0
        offset = 75
        textOffset = 90
        for i, levelName in enumerate(self.loadLevelNames()):
            if self.currSelectedLevel == i+1:
                color = (255, 255, 255)
            else:
                color = (150, 150, 150)
            if i < 3:
                self.dashboard.drawText(levelName, 175*i+textOffset, 100, 12)
                self.drawBorder(175*i+offset, 55, 125, 75, color, 5)
            else:
                self.dashboard.drawText(levelName, 175*j+textOffset, 250, 12)
                self.drawBorder(175*j+offset, 210, 125, 75, color, 5)
                j += 1

    def loadLevelNames(self):
        files = []
        res = []
        for r, d, f in os.walk("./levels"):
            for file in f:
                files.append(os.path.join(r, file))
        for f in files:
            res.append(os.path.split(f)[1].split(".")[0])
        self.levelCount = len(res)
        return res

    def checkInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.inChoosingLevel or self.inSettings:
                        self.inChoosingLevel = False
                        self.inSettings = False
                        self.__init__(self.screen, self.dashboard, self.level, self.sound)
                    else:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP or event.key == pygame.K_k:
                    if self.inChoosingLevel:
                        if self.currSelectedLevel > 3:
                            self.currSelectedLevel -= 3
                            self.drawLevelChooser()
                    if self.state > 0:
                        self.state -= 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_j:
                    if self.inChoosingLevel:
                        if self.currSelectedLevel+3 <= self.levelCount:
                            self.currSelectedLevel += 3
                            self.drawLevelChooser()
                    if self.state < 2:
                        self.state += 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_h:
                    if self.currSelectedLevel > 1:
                        self.currSelectedLevel -= 1
                        self.drawLevelChooser()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                    if self.currSelectedLevel < self.levelCount:
                        self.currSelectedLevel += 1
                        self.drawLevelChooser()
                elif event.key == pygame.K_RETURN:
                    if self.inChoosingLevel:
                        self.inChoosingLevel = False
                        self.dashboard.state = "start"
                        self.dashboard.time = 0
                        self.level.loadLevel(self.levelNames[self.currSelectedLevel-1])
                        self.dashboard.levelName = self.levelNames[self.currSelectedLevel-1].split("Level")[1]
                        self.start = True
                        return
                    if not self.inSettings:
                        if self.state == 0:
                            self.chooseLevel()
                        elif self.state == 1:
                            self.inSettings = True
                            self.state = 0
                        elif self.state == 2:
                            pygame.quit()
                            sys.exit()
                    else:
                        if self.state == 0:
                            if self.music:
                                self.sound.music_channel.stop()
                                self.music = False
                            else:
                                self.sound.music_channel.play(self.sound.soundtrack, loops=-1)
                                self.music = True
                            self.saveSettings("./settings.json")
                        elif self.state == 1:
                            if self.sfx:
                                self.sound.allowSFX = False
                                self.sfx = False
                            else:
                                self.sound.allowSFX = True
                                self.sfx = True
                            self.saveSettings("./settings.json")
                        elif self.state == 2:
                            self.inSettings = False
        pygame.display.update()
