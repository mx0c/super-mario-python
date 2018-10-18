
class jumpTrait:
    def __init__(self, entity):
        self.aVel = -12
        self.dVel = -6
        self.entity = entity
        self.startTime = 0

    def jump(self,jumping):
        if jumping:
            if not self.entity.inAir:
                self.entity.vel.y = self.aVel
                self.entity.inAir = True
        else:
            if self.entity.vel.y < self.dVel:
                self.entity.vel.y = self.dVel

    def reset(self):
        self.entity.inAir = False
