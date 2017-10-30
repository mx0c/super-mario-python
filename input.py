import pygame
from pygame.locals import *

def checkForInput(mario):
    keys = pygame.key.get_pressed()
    if(keys[K_LEFT] and not keys[K_RIGHT]):
        mario.goTrait.direction = -1
    elif(keys[K_RIGHT] and not keys[K_LEFT]):
        mario.goTrait.direction =  1
    else:
        mario.goTrait.direction =  0

    if(keys[K_SPACE]):
        mario.jumpTrait.start(mario)
    else:
        mario.jumpTrait.fall(mario)