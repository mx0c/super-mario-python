import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario
from classes.ProgressManager import ProgressManager

windowSize = 640, 480

class main:
    def _init_(self):
        self.exitmessage = 'restart'
        self.progress = ProgressManager()
        
    def run(self):
        while self.exitmessage == 'restart':
            pygame.mixer.pre_init(44100, -16, 2, 4096)
            pygame.init()
            screen = pygame.display.set_mode(windowSize)
            max_frame_rate = 60
            dashboard = Dashboard("./img/font.png", 8, screen)
            sound = Sound()
            level = Level(screen, sound, dashboard)
            menu = Menu(screen, dashboard, level, sound, self.progress)

            while not menu.start:
                menu.update()

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
                
            self.exitmessage = 'menu' if mario.exit_type == 'menu' else 'restart'

    def load_next_level(self):
        current = self.progress.highest_level
        next_level = f"1-{int(current.split('-')[1])+1}"
        if next_level in ["1-2", "1-3"]:  # Add more levels as needed
            self.progress.save_progress(next_level)
            self.exitmessage = 'restart'
        else:
            self.exitmessage = 'menu'

    def return_to_menu(self):
        self.exitmessage = 'menu'

if __name__ == "_main_":
    Main = main()
    Main.run()