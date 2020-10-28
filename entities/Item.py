from copy import copy

from classes.Dashboard import Dashboard
from classes.Maths import Vec2D


class Item(Dashboard):
    def __init__(self, collection, screen, x, y):
        super(Item, self).__init__("./img/font.png", 8, screen)
        self.ItemPos = Vec2D(x, y)
        self.itemVel = Vec2D(0, 0)
        self.screen = screen
        self.coin_animation = copy(collection.get("coin-item").animation)
        self.sound_played = False

    def spawnCoin(self, cam, sound, dashboard):
        if not self.sound_played:
            self.sound_played = True
            dashboard.points += 100
            sound.play_sfx(sound.coin)
        self.coin_animation.update()
        if self.coin_animation.timer < 45:
            if self.coin_animation.timer < 15:
                self.itemVel.y -= 0.5
                self.ItemPos.y += self.itemVel.y
            elif self.coin_animation.timer < 45:
                self.itemVel.y += 0.5
                self.ItemPos.y += self.itemVel.y
            self.screen.blit(
                self.coin_animation.image, (self.ItemPos.x + cam.x, self.ItemPos.y)
            )
        elif self.coin_animation.timer < 80:
            self.itemVel.y = -0.75
            self.ItemPos.y += self.itemVel.y
            self.drawText("100", self.ItemPos.x + 3 + cam.x, self.ItemPos.y, 8)
