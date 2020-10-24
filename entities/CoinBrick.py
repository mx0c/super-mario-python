from copy import copy

from entities.EntityBase import EntityBase
from entities.Item import Item


class CoinBrick(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, sound, dashboard, gravity=0):
        super(CoinBrick, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.image = self.spriteCollection.get("bricks").image
        self.type = "Block"
        self.triggered = False
        self.sound = sound
        self.dashboard = dashboard
        self.item = Item(spriteCollection, screen, self.rect.x, self.rect.y)

    def update(self, cam):
        if not self.alive or self.triggered:
            self.image = self.spriteCollection.get("empty").image
            self.item.spawnCoin(cam, self.sound, self.dashboard)
        self.screen.blit(
            self.spriteCollection.get("sky").image,
            (self.rect.x + cam.x, self.rect.y + 2),
        )
        self.screen.blit(self.image, (self.rect.x + cam.x, self.rect.y - 1))
