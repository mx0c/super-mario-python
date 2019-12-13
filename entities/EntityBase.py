import pygame

from classes.Maths import vec2D


class EntityBase(object):
    def __init__(self, x, y, gravity):
        self.vel = vec2D()
        self.rect = pygame.Rect(x * 32, y * 32, 32, 32)
        self.gravity = gravity
        self.traits = None
        self.alive = True
        self.timeAfterDeath = 5
        self.timer = 0
        self.type = ""
        self.onGround = False
        self.obeygravity = True
        
    def applyGravity(self):
        if self.obeygravity:
            self.vel.y += self.gravity

    def updateTraits(self):
        for trait in self.traits.values():
            try:
                trait.update()
            except AttributeError:
                pass

    def getPosIndex(self):
        return vec2D(int(self.rect.x / 32), int(self.rect.y / 32))

    def getPosIndexAsFloat(self):
        return vec2D(self.rect.x / 32.0, self.rect.y / 32.0)
