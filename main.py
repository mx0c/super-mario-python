import pygame
from pygame.locals import *
import spritesheet as sprite
from Level import Level
from mario import mario
import input

pygame.init()
screen = pygame.display.set_mode((640, 480))
max_frame_rate = 60

level = Level()
mario = mario(6,2,level.level,screen)
clock = pygame.time.Clock()

while (True):
    input.checkForInput(mario,level)
    level.drawLevel(screen)
    mario.drawMario()
    # update the screen
    pygame.display.update()
    clock.tick(max_frame_rate)


