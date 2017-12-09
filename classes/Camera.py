from classes.Maths import vec2D

class Camera():
    def __init__(self,pos):
        self.pos = vec2D(pos.x,pos.y)
        self.size = vec2D(10,10)