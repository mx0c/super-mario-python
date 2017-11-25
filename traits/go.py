import pygame
class goTrait():
    def __init__(self,animation,screen,camera,ent):
        self.animation = animation
        self.direction = 0
        self.heading = 1
        self.accelVel = 0.04
        self.decelVel = 0.02
        self.maxVel = 0.1
        self.screen = screen
        self.boost = False        
        self.camera = camera
        self.entity = ent
        
    def update(self):
        self.drawEntity()
        if(self.boost):
            self.maxVel = 0.2
        else:
            if(abs(self.entity.vel.x) > 0.1):
                self.entity.vel.x = 0.1 * self.heading
            self.maxVel = 0.1

        if(self.direction != 0):
            self.animation.update()
            #accelerate
            self.heading = self.direction
            if(abs(self.entity.vel.x) < self.maxVel):
                self.entity.vel.x += self.accelVel * self.heading
        else:
            self.animation.idle()
            #decelerate
            if(self.entity.vel.x >= 0):
                self.entity.vel.x -= self.decelVel
            else:
                self.entity.vel.x += self.accelVel
            if(self.entity.vel.x < 0):
                self.entity.vel.x = 0                

    def drawEntity(self):
        if(self.heading == 1):
            self.screen.blit(self.animation.image ,((self.camera.pos.x+self.entity.pos.x)*32,self.entity.pos.y*32))
        elif(self.heading == -1):
            self.screen.blit(pygame.transform.flip(self.animation.image,True,False),((self.camera.pos.x+self.entity.pos.x)*32,self.entity.pos.y*32))