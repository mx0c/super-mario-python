import spritesheet as sprite
import pygame

class sprites():
    def __init__(self):
        self.CharacterSpritesheet = sprite.spritesheet('img/characters.gif',16)
        self.TilesSpritesheet = sprite.spritesheet('img/tiles.png',16)
        #sprites
        self.mario = self.CharacterSpritesheet.image_at((276, 44, 16, 16),4, colorkey=-1)
        self.sky = self.TilesSpritesheet.image_at((48, 368, 16, 16),2)
        self.bricks = self.TilesSpritesheet.image_at((16,0,16,16),2)
        self.ground = self.TilesSpritesheet.image_at((0,0,16,16),2)
