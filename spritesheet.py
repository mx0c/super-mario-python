import pygame

class Spritesheet(object):
    def __init__(self, filename,tilesize=16):
        try:
            self.tilesize = tilesize
            self.sheet = pygame.image.load(filename)
            if(self.sheet.get_alpha()):
                self.sheet = self.sheet.convert_alpha()
            else:
                self.sheet = self.sheet.convert()
                self.sheet.set_colorkey((0,0,0))
        except pygame.error:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit
    def image_at(self, x, y, scalingfactor, colorkey = None, ignoreTileSize=False):
        if(ignoreTileSize):
            rect = pygame.Rect((x,y,self.tilesize,self.tilesize))
        else:
            rect = pygame.Rect((x*self.tilesize,y*self.tilesize,self.tilesize,self.tilesize))
        image = pygame.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return pygame.transform.scale(image,(self.tilesize*scalingfactor,self.tilesize*scalingfactor))
