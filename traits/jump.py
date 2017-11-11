class jumpTrait():
    def __init__(self):
        self.maxReached = False
        self.timer = 0
        self.jumpHeight = 7
        self.maxVel = 0.1
        self.vel = 0.05

    def start(self,mario):
        #initialy set Y-Vel to 0
        if(self.timer == 0):
            mario.vel.y = 0
        if(not self.maxReached):
            if(mario.vel.y < self.maxVel):
                mario.vel.y -= self.vel
                self.timer+=1
                if(self.timer > self.jumpHeight):
                    self.maxReached = True
        else:
            mario.applyGravity()
    
    def reset(self):
        self.timer = 0
        self.maxReached = False
                    
