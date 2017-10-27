import pygame
from pygame.locals import *
import spritesheet as sprite
import sprites
import mario
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

sprites = sprites.sprites()
mario = mario.mario(1,1)

while (True):
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

    for x in range(0,20):
        for y in range(0,13):
            screen.blit(sprites.sky,(x*32,y*32))
        for y in range(13,15):
            screen.blit(sprites.ground,(x*32,y*32))

    mario.drawMario(screen)
    # update the screen
    pygame.display.update()

