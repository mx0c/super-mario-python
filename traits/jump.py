class jumpTrait():
    def __init__(self,entity):
        self.maxReached = False
        self.timer = 0
        self.jumpHeight = 15
        self.maxVel = 6
        self.vel = 2
        self.jump = False
        self.entity = entity

    def start(self):
        #initialy set Y-Vel to 0
        if(self.timer == 0):
            self.entity.vel.y = 0
        if(not self.maxReached):
            if(self.entity.vel.y < self.maxVel):
                self.entity.vel.y -= self.vel
                self.timer+=1
            if(self.timer > self.jumpHeight):
                self.maxReached = True
    
    def reset(self):
        self.timer = 0
        self.maxReached = False
