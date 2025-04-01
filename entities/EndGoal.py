#added for group 32 project

import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, screen, sprite_collection, x, y, level):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_collection = sprite_collection
        self.image = self.sprite_collection.get("pipeR").image
        self.rect = pygame.Rect(x * 32, y * 32, 32, 64)
        self.screen = screen
        self.x = x
        self.y = y
        self.level = level
        self.triggered = False
        self.type = "Goal" 
        
    def update(self, camera):
        if not self.triggered:
            self.screen.blit(
                self.image, 
                ((self.x + camera.pos.x) * 32, self.y * 32)
            )

