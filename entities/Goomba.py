from classes.Sprites import Sprites
from classes.Animation import Animation
from classes.Maths import vec2D
from traits.leftrightwalk import LeftRightWalkTrait
from entities.EntityBase import EntityBase
import pygame


class Goomba(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level):
        super(Goomba, self).__init__(y, x - 1, 1.25)
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("goomba-1").image,
                                    self.spriteCollection.get("goomba-2").image])
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self, level)
        self.type = "Mob"
        self.dashboard = level.dashboard

    def update(self, camera):
        if(self.alive):
            self.applyGravity()
            self.screen.blit(
                self.animation.image,
                (self.rect.x + camera.x,
                 self.rect.y))
            self.animation.update()
            self.leftrightTrait.update()
        else:
            if(self.timer == 0):
                self.textPos = vec2D(self.rect.x + 3, self.rect.y)
            if(self.timer < self.timeAfterDeath):
                self.textPos.y += -0.5
                self.dashboard.drawText(
                    "100", self.textPos.x + camera.x, self.textPos.y, 8)
                self.screen.blit(self.spriteCollection.get(
                    "goomba-flat").image, (self.rect.x + camera.x, self.rect.y))
            else:
                self.alive = None
            self.timer += 0.1
