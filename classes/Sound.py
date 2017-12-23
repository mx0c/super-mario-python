import pygame
from pygame.mixer import Sound

class Sound():
    def __init__(self):
        self.music_channel = pygame.mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = pygame.mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)
        print(self.sfx_channel.get_volume(),self.music_channel.get_volume())
        self.soundtrack = pygame.mixer.Sound('./sfx/main_theme.ogg')
        self.coin = pygame.mixer.Sound('./sfx/coin.ogg')
        self.bump = pygame.mixer.Sound('./sfx/bump.ogg')
        self.stomp = pygame.mixer.Sound('./sfx/stomp.ogg')
        self.jump = pygame.mixer.Sound('./sfx/small_jump.ogg')
        self.death = pygame.mixer.Sound('./sfx/death.wav')

        #play soundtrack
        self.music_channel.play(self.soundtrack)
    
    def play_sfx(self,sfx):
        self.sfx_channel.play(sfx)
    
    def play_music(self,music):
        self.music_channel.play(music)


