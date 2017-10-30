class goTrait():
    def __init__(self):
        self.direction = 0
        self.acceleration = 0.00003
        self.decelaration = 0.00004
        self.maxSpeed = 0.02
        self.heading = 1
        
    def update(self,mario):
        if(self.direction != 0):
            #accelerate
            self.heading = self.direction
            if(abs(mario.vel.x) < self.maxSpeed):
                mario.vel.x += self.acceleration * self.heading
        else:
            #decelerate
            if(mario.vel.x > 0):
                mario.vel.x -= self.decelaration
            else:
                mario.vel.x += self.decelaration
            if(round(mario.vel.x,3) == 0):
                mario.vel.x = 0                

