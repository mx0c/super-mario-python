import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario


windowSize = 640, 480


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60

    # Buat dashboard, sound, level, menu
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    # Tunggu menu start
    while not menu.start:
        menu.update()

    # Buat Mario dulu
    mario = Mario(0, 0, level, screen, dashboard, sound)

    # Hubungkan Mario ke level dan dashboard
    level.mario = mario
    dashboard.mario = mario
    dashboard.level = level

    clock = pygame.time.Clock()

    # Loop utama game
    while not mario.restart:
        pygame.display.set_caption(
            "Super Mario running with {:d} FPS".format(int(clock.get_fps()))
        )

        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()

        pygame.display.update()
        clock.tick(max_frame_rate)

    return 'restart'


if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
