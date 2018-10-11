class Sprite:
    def __init__(self, image, colliding, animation=None, redrawBackground=False):
        self.image = image
        self.colliding = colliding
        self.animation = animation
        self.redrawBackground = redrawBackground

    def drawSprite(self, x, y, screen):
        dimensions = (x * 32, y * 32)
        if self.animation is None:
            screen.blit(self.image, dimensions)
        else:
            self.animation.update()
            screen.blit(self.animation.image, dimensions)
