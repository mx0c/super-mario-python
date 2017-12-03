from Sprites import Sprites
from Animation import Animation
import Maths
from traits.leftrightwalk import LeftRightWalkTrait

class Koopa():
    def __init__(self,screen,spriteColl,x,y,level):
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("goomba-1").image,
                                    self.spriteCollection.get("goomba-2").image])
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self,level,x,y)

    def update(self,camera):
        self.screen.blit(self.animation.image,((self.leftrightTrait.pos.x+camera.pos.x)*32,self.leftrightTrait.pos.y*32))
        self.animation.update()
        self.leftrightTrait.update()