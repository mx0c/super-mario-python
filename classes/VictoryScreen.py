#added for group 32 project
import pygame

class VictoryScreen:
    def __init__(self, screen, dashboard, sound, level_id):
        self.screen = screen
        self.dashboard = dashboard
        self.sound = sound
        self.level_id = level_id
        self.active = False
        self.timeout = 0
        self.return_to_menu = False
        
    def activate(self):
        self.active = True
        self.timeout = pygame.time.get_ticks() + 3000  #show screen for 3 seconds
        
    def update(self):
        if self.active:
            #creating the background
            overlay = pygame.Surface((640, 480))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))
            
            #victory message
            self.dashboard.drawText("Congratulations!", 180, 200, 24)
            self.dashboard.drawText("You Won!", 190, 250, 36)
            
            if pygame.time.get_ticks() > self.timeout:
                self.active = False
                self.return_to_menu = True
                
        return self.return_to_menu