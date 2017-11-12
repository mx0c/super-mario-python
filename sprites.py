import spritesheet as sprite
import pygame

class sprites():
    def __init__(self):
        self.CharacterSpritesheet = sprite.spritesheet('img/characters.gif',16)
        self.TilesSpritesheet = sprite.spritesheet('img/tiles.png',16)
        #sprites
        #charactersprites
        self.mario_idle = self.CharacterSpritesheet.image_at((276, 44, 16, 16),2, colorkey=-1)
        self.mario_run1 = self.CharacterSpritesheet.image_at((290, 44, 16, 16),2, colorkey=-1)
        self.mario_run2 = self.CharacterSpritesheet.image_at((304, 44, 16, 16),2, colorkey=-1)
        self.mario_run3 = self.CharacterSpritesheet.image_at((321, 44, 16, 16),2, colorkey=-1)
        self.mario_break = self.CharacterSpritesheet.image_at((337, 44, 16, 16),2, colorkey=-1)
        self.mario_jump = self.CharacterSpritesheet.image_at((355, 44, 16, 16),2, colorkey=-1)

        #background and object sprites
        self.sky = self.TilesSpritesheet.image_at((48, 368, 16, 16),2)
        self.bricks = self.TilesSpritesheet.image_at((16,0,16,16),2)
        self.ground = self.TilesSpritesheet.image_at((0,0,16,16),2)

        self.pipeL = self.TilesSpritesheet.image_at((0,8*16,16,16),2,colorkey=pygame.color.Color(255,255,255))
        self.pipeR = self.TilesSpritesheet.image_at((16,8*16,16,16),2,colorkey=pygame.color.Color(255,255,255))
        self.pipe2L = self.TilesSpritesheet.image_at((0,9*16,16,16),2,colorkey=pygame.color.Color(255,255,255))
        self.pipe2R =self.TilesSpritesheet.image_at((16,9*16,16,16),2,colorkey=pygame.color.Color(255,255,255))
