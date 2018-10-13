import pygame

from classes.Animation import Animation
from classes.Maths import vec2D
from entities.EntityBase import EntityBase
from traits.leftrightwalk import LeftRightWalkTrait


class Koopa(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level):
        super(Koopa, self).__init__(y - 1, x, 1.25)
        self.spriteCollection = spriteColl
        self.animation = Animation(
            [
                self.spriteCollection.get("koopa-1").image,
                self.spriteCollection.get("koopa-2").image,
            ]
        )
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self, level)
        self.timer = 0
        self.timeAfterDeath = 35
        self.type = "Mob"
        self.dashboard = level.dashboard

    def update(self, camera):
        if self.alive == True:
            self.updateAlive(camera)
        elif self.alive == "sleeping":
            self.sleepingInShell(camera)
        elif self.alive == "shellBouncing":
            self.shellBouncing(camera)
        elif self.alive == False:
            self.die(camera)

    def drawKoopa(self, camera):
        if self.leftrightTrait.direction == -1:
            self.screen.blit(
                self.animation.image, (self.rect.x + camera.x, self.rect.y - 32)
            )
        else:
            self.screen.blit(
                pygame.transform.flip(self.animation.image, True, False),
                (self.rect.x + camera.x, self.rect.y - 32),
            )

    def shellBouncing(self, camera):
        self.leftrightTrait.speed = 4
        self.applyGravity()
        self.animation.image = self.spriteCollection.get("koopa-hiding").image
        self.drawKoopa(camera)
        self.leftrightTrait.update()

    def die(self, camera):
        if self.timer == 0:
            self.textPos = vec2D(self.rect.x + 3, self.rect.y - 32)
        if self.timer < self.timeAfterDeath:
            self.textPos.y += -0.5
            self.dashboard.drawText("100", self.textPos.x + camera.x, self.textPos.y, 8)
            self.vel.y -= 0.5
            self.rect.y += self.vel.y
            self.screen.blit(
                self.spriteCollection.get("koopa-hiding").image,
                (self.rect.x + camera.x, self.rect.y - 32),
            )
        else:
            self.vel.y += 0.3
            self.rect.y += self.vel.y
            self.textPos.y += -0.5
            self.dashboard.drawText("100", self.textPos.x + camera.x, self.textPos.y, 8)
            self.screen.blit(
                self.spriteCollection.get("koopa-hiding").image,
                (self.rect.x + camera.x, self.rect.y - 32),
            )
            if self.timer > 500:
                # delete entity
                self.alive = None
        self.timer += 6

    def sleepingInShell(self, camera):
        if self.timer < self.timeAfterDeath:
            self.screen.blit(
                self.spriteCollection.get("koopa-hiding").image,
                (self.rect.x + camera.x, self.rect.y - 32),
            )
        else:
            self.alive = True
            self.timer = 0
        self.timer += 0.1

    def updateAlive(self, camera):
        self.applyGravity()
        self.drawKoopa(camera)
        self.animation.update()
        self.leftrightTrait.update()
