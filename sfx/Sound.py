import pygame
from pygame.mixer import Sound

class ChannelManager(object):
    def __init__(self,channels):
        pygame.mixer.set_num_channels(channels)
        self.channels = []
        for i in range(0,channels):
            self.channels.append(pygame.mixer.Channel(i))
        
    def getChannel(self):
        for channel in self.channels:
            if not channel.get_busy():
                return channel
    
    def shutdown(self):
        for channel in self.channels:
            channel.stop()

class Sound(ChannelManager):
    def __init__(self):
        super(Sound,self).__init__(25)
        self.soundtrack = pygame.mixer.Sound('./sfx/main_theme_sped_up.ogg')
        self.getChannel().play(self.soundtrack)
        
        self.coin = pygame.mixer.Sound('./sfx/coin.ogg')
        self.bump = pygame.mixer.Sound('./sfx/bump.ogg')
        self.stomp = pygame.mixer.Sound('./sfx/stomp.ogg')
    
    def play_sfx(self,sfx):
        self.getChannel().play(sfx)



