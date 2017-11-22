from Sprites import Sprites
import pygame
from pygame.locals import *
import Maths
from traits import go,jump
from traits.go import goTrait
from traits.jump import jumpTrait
from Animation import Animation
from Collission_Detection import Collided,Collision
from Camera import Camera

class Mario():
    def __init__(self,x,y,level,screen,gravity=0.04):
        self.pos = Maths.vec2D(x,y)
        self.vel = Maths.vec2D()
        self.gravity = gravity
        self.spritesObj = Sprites()
        self.jumpTrait = jumpTrait()
        self.camera = Camera(self.pos)
        self.animation = Animation([
            self.spritesObj.characterSprites["mario_run1"].image,
            self.spritesObj.characterSprites["mario_run2"].image,
            self.spritesObj.characterSprites["mario_run3"].image
        ],self.spritesObj.characterSprites["mario_idle"].image)
        self.goTrait = goTrait(self.animation,screen)
        self.level = level
        self.collision = Collision(self,level)

    def applyGravity(self):
        self.vel.y += self.gravity

    def drawMario(self):
        self.goTrait.update(self)
        self.moveMario()

    def debug(self):
        print(self.pos.x, self.pos.y, self.vel.x, self.vel.y)

    def moveMario(self):
        self.pos.y += self.vel.y
        self.pos.x += self.vel.x
        self.camera.pos.x = -self.pos.x+9
        self.collision.checkCollision()