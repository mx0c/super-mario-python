from copy import copy

from entities.EntityBase import EntityBase


class Coin(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, gravity=0):
        super(Coin, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = copy(self.spriteCollection.get("coin").animation)
        self.type = "Item"

    def update(self, cam):
        if self.alive:
            self.animation.update()
            self.screen.blit(self.animation.image, (self.rect.x + cam.x, self.rect.y))
