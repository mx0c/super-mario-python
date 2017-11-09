import pygame
from pygame.locals import *
import spritesheet as sprite
from drawLevel import drawLevel
from mario import mario
import sys
import input

pygame.init()
screen = pygame.display.set_mode((640, 480))
max_frame_rate = 60

levelLoader = drawLevel()
mario = mario(6,2,levelLoader.level,screen)
clock = pygame.time.Clock()

while (True):
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    input.checkForInput(mario)
    levelLoader.drawLevel(screen)
    mario.drawMario()
    # update the screen
    pygame.display.update()
    clock.tick(max_frame_rate)


