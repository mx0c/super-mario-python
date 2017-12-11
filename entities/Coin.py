from entities.EntityBase import EntityBase
from classes.Animation import Animation

class Coin(EntityBase):
    def __init__(self,screen,spriteCollection,x,y):
        super(Coin,self).__init__(y,x,0)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = self.spriteCollection.get('coin').animation


    def update(self,cam):
        self.animation.update()