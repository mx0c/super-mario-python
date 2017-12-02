import pygame
from pygame.locals import *
from Level import Level
import sys

def checkForInput(mario,level):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT and event.key != pygame.K_RIGHT:
                mario.traits['goTrait'].direction = -1
            elif event.key == pygame.K_RIGHT and event.key != pygame.K_LEFT:
                mario.traits['goTrait'].direction =  1
            if event.key == K_LSHIFT:
                mario.traits['goTrait'].boost = True
            if event.key == K_SPACE:
                mario.traits['jumpTrait'].jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                mario.traits['goTrait'].direction =  0
            if event.key == pygame.K_LSHIFT:
                mario.traits['goTrait'].boost = False
            if event.key == K_SPACE:
                mario.traits['jumpTrait'].jump = False
 
def moveMarioWithMouse(mario):
    mouseX = pygame.mouse.get_pos()[0]/32
    mouseY = pygame.mouse.get_pos()[1]/32
    if pygame.mouse.get_pressed()[2]:
        mario.camera.pos.x = -mouseX
    if pygame.mouse.get_pressed()[0]:
        mario.vel.x = 0
        mario.vel.y = 0       
        print(mario.pos.x,mario.pos.y)
        mario.pos.x = mouseX-mario.camera.pos.x
        mario.pos.y = mouseY 
        

    