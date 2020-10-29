from copy import copy

from entities.EntityBase import EntityBase
from entities.Item import Item


class CoinBox(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, sound, dashboard, gravity=0):
        super(CoinBox, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = copy(self.spriteCollection.get("CoinBox").animation)
        self.type = "Block"
        self.triggered = False
        self.time = 0
        self.maxTime = 10
        self.sound = sound
        self.dashboard = dashboard
        self.vel = 1
        self.item = Item(spriteCollection, screen, self.rect.x, self.rect.y)

    def update(self, cam):
        if self.alive and not self.triggered:
            self.animation.update()
        else:
            self.animation.image = self.spriteCollection.get("empty").image
            self.item.spawnCoin(cam, self.sound, self.dashboard)
            if self.time < self.maxTime:
                self.time += 1
                self.rect.y -= self.vel
            else:
                if self.time < self.maxTime * 2:
                    self.time += 1
                    self.rect.y += self.vel
        self.screen.blit(
            self.spriteCollection.get("sky").image,
            (self.rect.x + cam.x, self.rect.y + 2),
        )
        self.screen.blit(self.animation.image, (self.rect.x + cam.x, self.rect.y - 1))
