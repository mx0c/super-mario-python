class goTrait():
    def __init__(self):
        self.direction = 0
        self.heading = 1
        self.maxVel = 0.3
        self.vel = 0.03
        
    def update(self,mario):
        if(self.direction != 0):
            #accelerate
            self.heading = self.direction
            if(abs(mario.vel.x) < self.maxVel):
                mario.vel.x += self.vel * self.heading
        else:
            #decelerate
            if(mario.vel.x >= 0):
                mario.vel.x -= self.vel
            else:
                mario.vel.x += self.vel
            #round to zero
            if(round(mario.vel.x,1) == 0):
                mario.vel.x = 0                

