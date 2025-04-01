import pygame
from classes.LevelCommands import ContinueCommand, CancelCommand

class VictoryScreen:
    def _init_(self, screen, dashboard, sound, level_id, game_main):
        self.screen = screen
        self.dashboard = dashboard
        self.sound = sound
        self.level_id = level_id
        self.game_main = game_main
        self.active = False
        self.option = 0  # 0=Continue, 1=Cancel
        self.commands = [
            ContinueCommand(game_main),
            CancelCommand(game_main)
        ]

    def activate(self):
        self.active = True
        
    def update(self):
        if self.active:
            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.option = 0
                    elif event.key == pygame.K_RIGHT:
                        self.option = 1
                    elif event.key == pygame.K_RETURN:
                        self.commands[self.option].execute()
                        return True

            overlay = pygame.Surface((640, 480))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))
            
            self.dashboard.drawText("Congratulations!", 180, 200, 24)
            self.dashboard.drawText("You Won!", 180, 200, 36)
            self.dashboard.drawText("Continue", 200, 300, 24, 
                color=(255,255,0) if self.option==0 else (255,255,255))
            self.dashboard.drawText("Quit", 400, 300, 24,
                color=(255,255,0) if self.option==1 else (255,255,255))
            
            pygame.display.update()
        return False


