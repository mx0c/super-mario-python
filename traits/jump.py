
class jumpTrait:
    def __init__(self, entity):
        self.vertical_speed = -12 #jump speed
        self.jumpHeight = 120 #jump height in pixels
        self.entity = entity
        self.initalHeight = 384 #stores the position of mario at jump
        self.deaccelerationHeight = self.jumpHeight - ((self.vertical_speed*self.vertical_speed)/(2*self.entity.gravity))

    def jump(self,jumping):
        print(self.entity.rect.y)
        if jumping:
            if not self.entity.inAir and not self.entity.inJump: #only jump when mario is on ground and not in a jump. redundant check
                self.entity.sound.play_sfx(self.entity.sound.jump)
                self.entity.vel.y = self.vertical_speed
                self.entity.inAir = True
                self.initalHeight = self.entity.rect.y
                self.entity.inJump = True
                self.entity.obeygravity = False #dont obey gravity in jump so as to reach jump height no matter what the speed

        if self.entity.inJump: #check vertical distance travelled while mario is in a jump
            if (self.initalHeight-self.entity.rect.y) >= self.deaccelerationHeight or self.entity.vel.y==0:
                print("reached")
                self.entity.inJump = False
                self.entity.obeygravity = True #mario obeys gravity again and continues normal play


    def reset(self):
        self.entity.inAir = False
