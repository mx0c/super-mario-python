import pygame
class goTrait():
    def __init__(self,animation,screen):
        self.animation = animation
        self.direction = 0
        self.heading = 1
        self.maxVel = 0.5
        self.vel = 0.04
        self.screen = screen
        
    def update(self,mario):
        if(self.heading == 1):
            self.screen.blit(self.animation.image ,(mario.pos.x*32,mario.pos.y*32))
        elif(self.heading == -1):
            self.screen.blit(pygame.transform.flip(self.animation.image,True,False),(mario.pos.x*32,mario.pos.y*32))
        
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

