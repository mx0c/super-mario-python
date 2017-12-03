from Sprites import Sprites
from Animation import Animation
import Maths
from traits.leftrightwalk import LeftRightWalkTrait
from entities.EntityBase import EntityBase

class Goomba(EntityBase):
    def __init__(self,screen,spriteColl,x,y,level):
        super(Goomba,self).__init__(y,x-1,0.04)
        self.spriteCollection = spriteColl
        self.animation = Animation([self.spriteCollection.get("goomba-1").image,
                                    self.spriteCollection.get("goomba-2").image])
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self,level)

    def update(self,camera):
        self.applyGravity()
        self.screen.blit(self.animation.image,((self.pos.x+camera.pos.x)*32,self.pos.y*32))
        self.animation.update()
        self.leftrightTrait.update()
        