import pygame
from pygame.locals import *
import classes.Spritesheet as Sprite
from classes.Level import Level
from entities.Mario import Mario
from classes.Input import Input
from classes.Dashboard import Dashboard

def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    max_frame_rate = 60

    level = Level(screen)
    dashboard = Dashboard("./img/font.png",8,screen)
    mario = Mario(0,0,level,screen,dashboard)
    input = Input(mario)
    clock = pygame.time.Clock()

    while (not mario.restart):
        pygame.display.set_caption("{:.2f} FPS".format(clock.get_fps()))
        level.drawLevel(mario.camera)
        dashboard.update()
        input.checkForInput()
        mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    mario.sound.shutdown()
    main()

if __name__ == "__main__":
    main()



