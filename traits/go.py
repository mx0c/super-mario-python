import pygame
class goTrait():
    def __init__(self,animation,screen,camera):
        self.animation = animation
        self.direction = 0
        self.heading = 1
        self.vel = 0.03
        self.maxVel = 0.1
        self.screen = screen
        self.boost = False        
        self.camera = camera
        
    def update(self,mario):
        if(self.heading == 1):
            self.screen.blit(self.animation.image ,((self.camera.pos.x+mario.pos.x)*32,mario.pos.y*32))
        elif(self.heading == -1):
            self.screen.blit(pygame.transform.flip(self.animation.image,True,False),((self.camera.pos.x+mario.pos.x)*32,mario.pos.y*32))
        
        if(self.boost):
            self.maxVel = 0.2
        else:
            if(abs(mario.vel.x) > 0.1):
                mario.vel.x = 0.1 * self.heading
            self.maxVel = 0.1

        if(self.direction != 0):
            self.animation.update()
            #accelerate
            self.heading = self.direction
            if(abs(mario.vel.x) < self.maxVel):
                mario.vel.x += self.vel * self.heading
        else:
            self.animation.idle()
            #decelerate
            if(mario.vel.x >= 0):
                mario.vel.x -= self.vel
            else:
                mario.vel.x += self.vel
            #round to zero
            if(round(mario.vel.x,1) == 0):
                mario.vel.x = 0                

