from copy import copy
#edit-for coin new branch for merging 
from entities.EntityBase import EntityBase
from classes.GameManager import GameManager  # Import GameManager to manage coins

class Coin(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, gravity=0):
        super(Coin, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = copy(self.spriteCollection.get("coin").animation)
        self.type = "Item"

    def update(self, cam):
        """Updates coin animation."""
        if self.alive:
            self.animation.update()
            self.screen.blit(self.animation.image, (self.rect.x + cam.x, self.rect.y))

    def collect(self, mario):
        """Removes coin and updates GameManager."""
        self.alive = False  # Remove coin from game
        mario.dashboard.coins += 1  # Increase Mario's coin count
        GameManager().save_coin_count(mario.dashboard.coins)  # Persist coin count

