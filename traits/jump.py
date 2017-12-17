class jumpTrait():
    def __init__(self,entity):
        self.maxReached = False
        self.timer = 0
        self.jumpHeight = 7
        self.maxVel = 5
        self.vel = 2
        self.inAir = False
        self.entity = entity
        self.sound_played = False

    def start(self):
        if(not self.sound_played):
              self.entity.sound.play_sfx(self.entity.sound.jump)
              self.sound_played = True
        if(not self.maxReached and not self.entity.traits["bounceTrait"].jump):
            self.inAir = True
            self.entity.gravity = 0
            self.timer+=1
            if(self.entity.vel.y < self.maxVel):
                self.entity.vel.y -= self.vel
            if(self.timer > self.jumpHeight):
                self.maxReached = True
                self.sound_played = False
                self.entity.gravity = 1.00
    
    def reset(self):
        self.timer = 0
        self.maxReached = False
        self.inAir = False
