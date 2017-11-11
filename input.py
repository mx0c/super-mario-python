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
        mario.applyGravity()

    if(keys[K_LSHIFT]):
        mario.goTrait.boost = True
    else:
        mario.goTrait.boost = False
 
    if pygame.mouse.get_pressed()[0]:
        mario.vel.x = 0
        mario.vel.y = 0       
        print(mario.pos.x,mario.pos.y)
        mario.pos.x = int(pygame.mouse.get_pos()[0]/32)
        mario.pos.y = int(pygame.mouse.get_pos()[1]/32)