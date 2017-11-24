from Sprites import Sprites
from Animation import Animation
import Maths

class Goomba():
    def __init__(self,screen,spriteColl):
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("goomba-1"),self.spriteCollection.get("goomba-2")])
        self.pos = Maths.vec2D()
        self.screen = screen

    def update(self):
        self.screen.blit(self.animation.image,self.pos.x*32,self.pos.y*32)
        self.animation.update()

    def spawnGoomba(self,x,y):
        self.pos = Maths.vec2D(x,y)
        self.update()