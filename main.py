import pygame
from pygame.locals import *
import spritesheet as sprite
import drawLevel
import mario
import sys
import input

pygame.init()
screen = pygame.display.set_mode((640, 480))

levelLoader = drawLevel.drawLevel()
mario = mario.mario(7,10,levelLoader.level)

while (True):
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    input.checkForInput(mario)

    levelLoader.drawLevel(screen)

    mario.drawMario(screen)
    # update the screen
    pygame.display.update()


