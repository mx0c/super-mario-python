class JumpTrait:
    def __init__(self, entity):
        self.vertical_speed = -12
        self.jumpHeight = 120
        self.entity = entity
        self.initalHeight = 384
        self.deaccelerationHeight = self.jumpHeight - ((self.vertical_speed*self.vertical_speed)/(2*self.entity.gravity))

    def jump(self, jumping):
        if jumping:
            if not self.entity.inAir and not self.entity.inJump:  # redundant check
                self.entity.sound.play_sfx(self.entity.sound.jump)
                self.entity.vel.y = self.vertical_speed
                self.entity.inAir = True
                self.initalHeight = self.entity.rect.y
                self.entity.inJump = True
                self.entity.obeyGravity = False  # always reach maximum height

        if self.entity.inJump:
            if (self.initalHeight-self.entity.rect.y) >= self.deaccelerationHeight or self.entity.vel.y == 0:
                self.entity.inJump = False
                self.entity.obeyGravity = True

    def reset(self):
        self.entity.inAir = False
