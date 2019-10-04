
class jumpTrait:
    def __init__(self, entity):
        self.aVel = -14
        self.dVel = -10
        self.entity = entity
        self.startTime = 0

    def jump(self,jumping):
        if jumping:
            if not self.entity.inAir:
                self.entity.sound.play_sfx(self.entity.sound.jump)
                self.entity.vel.y = self.aVel
                self.entity.inAir = True
        else:
            if self.entity.vel.y < self.dVel:
                self.entity.vel.y = self.dVel

    def reset(self):
        self.entity.inAir = False
