
class EntityCollider():
    def __init__(self,entity):
        self.entity = entity

    def check(self,target):
        if self.entity.rect.colliderect(target.rect):
            return self.determineSide(target.rect,self.entity.rect)
        return False
            
    def determineSide(self,rect1, rect2):
        if(rect1.collidepoint(rect2.bottomleft) or rect1.collidepoint(rect2.bottomright) or rect1.collidepoint(rect2.midbottom)):
            if(rect2.collidepoint(rect1.midleft) or rect2.collidepoint(rect1.midright)):
                return True
            else:
                if(self.entity.vel.y > 0):
                    return "top"
        return True
