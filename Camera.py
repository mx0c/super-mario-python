import Maths

class Camera():
    def __init__(self,pos):
        self.pos = Maths.vec2D(pos.x,pos.y)
        self.size = Maths.vec2D(10,10)