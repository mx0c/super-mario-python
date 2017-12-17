import pygame
from pygame.mixer import Sound

class Sound():
    def __init__(self):
        self.sountrack_player = pygame.mixer.Channel(0)
        self.soundtrack = pygame.mixer.Sound('./sfx/main_theme_sped_up.ogg')
        self.sountrack_player.play(self.soundtrack)
        
        self.sfx_player = pygame.mixer.Channel(1)
        self.coin = pygame.mixer.Sound('./sfx/coin.ogg')
        self.bump = pygame.mixer.Sound('./sfx/bump.ogg')
        self.jump = pygame.mixer.Sound('./sfx/small_jump.ogg')

        self.play_sfx = lambda sfx: self.sfx_player.play(sfx)