import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario


windowSize = 640, 480


def main(levelToLoad=None):
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    if levelToLoad is None:
        while not menu.start:
            menu.update()
        levelToLoad = menu.levelNames[menu.currSelectedLevel - 1]
        level.loadLevel(levelToLoad)
    else:
        level.loadLevel(levelToLoad)

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption("Super Mario running with {:d} FPS".format(int(clock.get_fps())))
        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    
    # Check if level was completed or if player died
    if mario.levelComplete:
        # Load next level
        levelNames = menu.loadLevelNames()
        currentLevelIndex = levelNames.index(levelToLoad)
        if currentLevelIndex + 1 < len(levelNames):
            nextLevel = levelNames[currentLevelIndex + 1]
            return ('nextLevel', nextLevel)
        else:
            # All levels completed
            return 'gameComplete'
    
    return 'restart'


if __name__ == "__main__":
    result = ('nextLevel', None)
    while result == 'restart' or (isinstance(result, tuple) and result[0] == 'nextLevel'):
        if isinstance(result, tuple) and result[0] == 'nextLevel':
            result = main(result[1])
        else:
            result = main()
