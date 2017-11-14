import pygame
from pygame.locals import *
import spritesheet as sprite
from Level import Level
from mario import mario
import sys
import input
from Editor import Editor

pygame.init()
screen = pygame.display.set_mode((640, 480))
max_frame_rate = 60

level = Level()
mario = mario(6,2,level.level,screen)
clock = pygame.time.Clock()
editor = Editor(level,screen)

while (True):
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    input.checkForInput(mario,editor)
    level.drawLevel(screen)
    mario.drawMario()
    editor.checkUserInput()
    # update the screen
    pygame.display.update()
    clock.tick(max_frame_rate)


