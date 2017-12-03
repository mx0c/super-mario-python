import Maths

class EntityBase():
    def __init__(self,x,y,gravity):
        self.pos = Maths.vec2D(x,y)
        self.vel = Maths.vec2D()
        self.gravity = gravity
        self.traits = None

    def applyGravity(self):
         self.vel.y += self.gravity

    def updateTraits(self):
        for trait in self.traits.values():
            try:
                trait.update()
            except Exception:
                pass