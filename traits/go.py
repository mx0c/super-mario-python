import pygame
class goTrait():
    def __init__(self,animation,screen,camera,ent):
        self.animation = animation
        self.direction = 0
        self.heading = 1
        self.accelVel = 0.015
        self.decelVel = 0.010
        self.maxVel = 0.1
        self.screen = screen
        self.boost = False        
        self.camera = camera
        self.entity = ent
        
    def update(self): 
        if(self.boost):
            self.maxVel = 0.2
        else:
            if(abs(self.entity.vel.x) > 0.1):
                self.entity.vel.x = 0.1 * self.heading
            self.maxVel = 0.1

        if(self.direction != 0):
            self.heading = self.direction
            if(self.heading == 1):
                if(self.entity.vel.x < self.maxVel):
                    self.entity.vel.x += self.accelVel * self.heading
            else:
                if(self.entity.vel.x > -self.maxVel):
                    self.entity.vel.x += self.accelVel * self.heading
            self.animation.update()
        else:
            self.animation.idle()
            if(self.entity.vel.x >= 0):
                self.entity.vel.x -= self.decelVel
            else:
                self.entity.vel.x += self.decelVel
            if(round(self.entity.vel.x,1) == 0):
                self.entity.vel.x = 0           
        self.drawEntity()     
    
    def drawEntity(self):
        if(self.heading == 1):
            self.screen.blit(self.animation.image ,(self.camera.pos.x*32+self.entity.rect.x,self.entity.rect.y))
        elif(self.heading == -1):
            self.screen.blit(pygame.transform.flip(self.animation.image,True,False),(self.camera.pos.x*32+self.entity.rect.x,self.entity.rect.y))