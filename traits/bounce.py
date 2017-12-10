class bounceTrait():
    def __init__(self,entity):
        self.maxReached = False
        self.timer = 0
        self.jumpHeight = 5
        self.maxVel = 8
        self.vel = 3.5
        self.jump = False
        self.entity = entity

    def update(self):
        #initialy set Y-Vel to 0
        if(self.jump):
            if(self.timer == 0):
                self.entity.vel.y = 0
            if(not self.maxReached):
                if(self.entity.vel.y < self.maxVel):
                    self.entity.vel.y -= self.vel
                    self.timer+=1
                if(self.timer > self.jumpHeight):
                    self.maxReached = True
            else:
                self.reset()
    
    def reset(self):
        self.timer = 0
        self.maxReached = False
        self.jump = False
