from baseTrait import baseTrait

class jumpTrait(baseTrait):
    def __init__(self):
        self.maxReached = False
        self.vel = 0.0005
        self.maxVel = 0.01
        self.timer = 0
        self.jumpHeight = 120 

    def start(self,mario):
        if(not self.maxReached):
            if(mario.vel.y < self.maxVel):
                mario.vel.y -= self.vel
                self.timer+=1
                if(self.timer > self.jumpHeight):
                    self.maxReached = True
        else:
            mario.applyGravity()
                    
