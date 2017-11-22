import pygame
from pygame.locals import *
import Spritesheet as Sprite
from Level import Level
from Mario import Mario
import input

pygame.init()
screen = pygame.display.set_mode((640, 480))
max_frame_rate = 60

level = Level(screen)
mario = Mario(0,0,level.level,screen)
clock = pygame.time.Clock()

while (True):
    input.checkForInput(mario,level)
    pygame.display.set_caption("{:.2f} FPS".format(clock.get_fps()))
    level.drawLevel(mario.camera)
    mario.drawMario()
    # update the screen
    pygame.display.update()
    clock.tick(max_frame_rate)


