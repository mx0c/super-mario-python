class jumpTrait():
    def __init__(self):
        self.maxReached = False
        self.vel = 0.0005
        self.maxVel = 0.01
        self.timer = 0
        self.jumpHeight = 125

    def start(self,mario):
        if(not self.maxReached):
            if(mario.vel.y < self.maxVel):
                mario.vel.y -= self.vel
                self.timer+=1
                if(self.timer > self.jumpHeight):
                    self.maxReached = True
        else:
            self.fall(mario)

    def fall(self,mario):
        if(mario.pos.y < 11):
            mario.vel.y += self.vel
        else:  
            mario.vel.y = 0
            self.timer = 0
            self.maxReached = False
