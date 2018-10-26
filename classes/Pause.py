import pygame
import sys

from classes.Spritesheet import Spritesheet


class Pause:

    def __init__(self, screen, entity, dashboard):
        self.screen = screen
        self.entity = entity
        self.dashboard = dashboard
        self.state = 0
        self.spritesheet = Spritesheet("./img/title_screen.png")
        self.pause_rect = pygame.rect.Rect(50, 80, 540, 350)
        self.dot = self.spritesheet.image_at(
            0, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )

    def update(self):
        self.screen.fill(0, self.pause_rect)
        self.dashboard.drawText("PAUSED", 176, 160, 48)
        self.dashboard.drawText("CONTINUE", 180, 280, 20)
        self.dashboard.drawText("BACK TO MENU", 180, 320, 20)
        self.drawDot()
        pygame.display.update()
        self.checkInput()

    def drawDot(self):
        if self.state == 0:
            self.screen.blit(self.dot, (145, 270))
        elif self.state == 1:
            self.screen.blit(self.dot, (145, 310))

    def checkInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.state == 0:
                        self.entity.pause = False
                    elif self.state == 1:
                        self.entity.restart = True
                elif event.key == pygame.K_UP:
                    if self.state > 0:
                        self.state -= 1
                elif event.key == pygame.K_DOWN:
                    if self.state < 1:
                        self.state += 1
