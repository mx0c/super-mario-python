from entities.EntityBase import EntityBase
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Animation import Animation
from entities.EntityBase import EntityBase
from classes.Maths import Vec2D

class FireFlower(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level, sound):
        super(FireFlower, self).__init__(y, x , 0)
        self.spriteCollection = spriteColl
        self.animation = self.spriteCollection.get("FireFlower").animation
        self.screen = screen
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level
        self.type = "item"
        self.dashboard = level.dashboard
        self.sound = sound

    def update(self, camera):
        if self.alive:
            self.drawFireFlower(camera)
        else:
            self.alive = None

    def drawFireFlower(self, camera):
        self.screen.blit(self.animation.image, (self.rect.x + camera.x, self.rect.y))
        self.animation.update()



        