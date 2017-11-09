class jumpTrait():
    def __init__(self):
        self.maxReached = False
        self.timer = 0
        self.jumpHeight = 5
        self.maxVel = 0.1
        self.vel = 0.05

    def start(self,mario):
        if(not self.maxReached):
            if(mario.vel.y < self.maxVel):
                mario.vel.y -= self.vel
                self.timer+=1
                if(self.timer > self.jumpHeight):
                    self.maxReached = True
        else:
            mario.applyGravity()
                    
