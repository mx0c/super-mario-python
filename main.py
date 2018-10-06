import pygame
from pygame.locals import *
import classes.Spritesheet as Sprite
from classes.Level import Level
from entities.Mario import Mario
from classes.Input import Input
from classes.Dashboard import Dashboard
from classes.Sound import Sound
from classes.Menu import Menu


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    max_frame_rate = 60

    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    while(not menu.start):
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while (not mario.restart):
        pygame.display.set_caption("{:.2f} FPS".format(clock.get_fps()))
        level.drawLevel(mario.camera)
        dashboard.update()
        mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    main()


if __name__ == "__main__":
    main()
