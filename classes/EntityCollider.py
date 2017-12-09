
class EntityCollider():
    def __init__(self,entity):
        self.entity = entity

    def check(self,target):
        if self.entity.rect.colliderect(target.rect):
            return True
            
    