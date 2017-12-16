from classes.Maths import vec2D

class Camera():
    def __init__(self,pos,entity):
        self.pos = vec2D(pos.x,pos.y)
        self.entity = entity

    def move(self):
        xPosFloat = self.entity.getPosIndex(True).x
        if xPosFloat > 10 and xPosFloat < 50:
            self.pos.x = -xPosFloat+10


