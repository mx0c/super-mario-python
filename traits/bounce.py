class bounceTrait:
    def __init__(self, entity):
        self.vel = 5
        self.jump = False
        self.entity = entity

    def update(self):
        if self.jump:
            self.entity.vel.y = 0
            self.entity.vel.y -= self.vel
            self.jump = False
            self.entity.inAir = True

    def reset(self):
        self.entity.inAir = False
