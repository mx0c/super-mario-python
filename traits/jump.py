class jumpTrait():
    def __init__(self, entity):
        self.maxReached = False
        self.timer = 0
        self.jumpHeight = 5
        self.maxVel = 5
        self.vel = 4
        self.inAir = False
        self.entity = entity

    def start(self):
        if(not self.inAir):
            self.entity.sound.play_sfx(self.entity.sound.jump)
        if(not self.maxReached and not self.entity.traits["bounceTrait"].jump):
            self.inAir = True
            self.timer += 1
            if(self.entity.vel.y < self.maxVel):
                self.entity.vel.y -= self.vel
            # Maximum reached
            if(self.timer > self.jumpHeight):
                self.maxReached = True

    def reset(self):
        self.timer = 0
        self.maxReached = False
        self.inAir = False
