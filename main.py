import pygame
from pygame.locals import *
import spritesheet as sprite
import sprites
import mario
import sys

mario = mario.mario(1,1)
while (True):
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

    for x in range(0,20):
        for y in range(0,13):
            sprites.screen.blit(sprites.sky,(x*32,y*32))
        for y in range(13,15):
            sprites.screen.blit(sprites.ground,(x*32,y*32))


    mario.drawMario()
    # update the screen
    pygame.display.update()

