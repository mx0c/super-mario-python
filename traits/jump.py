from pygame.time import get_ticks

class jumpTrait:
    def __init__(self, entity):
        self.vel = -6
        self.entity = entity
        self.startTime = 0
        self.maxTime = 300

    def jump(self, jumping):
        if (jumping and self.entity.onGround):
            self.startTime = get_ticks()
        if (jumping and get_ticks() - self.startTime < self.maxTime):
            self.entity.vel.y = self.vel
            self.entity.inAir = True

    def reset(self):
        self.entity.inAir = False
