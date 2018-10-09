class jumpTrait():
    def __init__(self, entity):
        self.vel = 15
        self.entity = entity
        
    def start(self):
        if(not self.entity.inAir):
            self.entity.sound.play_sfx(self.entity.sound.jump)
        if(not self.entity.inAir):
            if(not self.entity.inAir):
                self.entity.vel.y -= self.vel
                self.entity.inAir = True

    def reset(self):
        self.entity.inAir = False
