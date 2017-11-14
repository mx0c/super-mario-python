from spritesheet import spritesheet
import pygame
from sprite import sprite

class sprites():
    def __init__(self):
        self.CharacterSpritesheet = spritesheet('img/characters.gif',16)
        self.TilesSpritesheet = spritesheet('img/tiles.png',16)
       
        #sprites
        #charactersprites
        self.characterSprites = {
            "mario_idle": sprite(self.CharacterSpritesheet.image_at((276, 44, 16, 16),2, colorkey=-1),True),
            "mario_run1": sprite(self.CharacterSpritesheet.image_at((290, 44, 16, 16),2, colorkey=-1),True),
            "mario_run2": sprite(self.CharacterSpritesheet.image_at((304, 44, 16, 16),2, colorkey=-1),True),
            "mario_run3": sprite(self.CharacterSpritesheet.image_at((321, 44, 16, 16),2, colorkey=-1),True),
            "mario_break": sprite(self.CharacterSpritesheet.image_at((337, 44, 16, 16),2, colorkey=-1),True),
            "mario_jump": sprite(self.CharacterSpritesheet.image_at((355, 44, 16, 16),2, colorkey=-1),True)
        }

        self.backgroundSprites = {
            "sky": sprite(self.TilesSpritesheet.image_at((48, 368, 16, 16),2),False),
            "bricks": sprite(self.TilesSpritesheet.image_at((16,0,16,16),2),True),
            "ground": sprite(self.TilesSpritesheet.image_at((0,0,16,16),2),True),
            "pipeL": sprite(self.TilesSpritesheet.image_at((0,10*16,16,16),2),True),
            "pipeR": sprite(self.TilesSpritesheet.image_at((16,10*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),True),
            "pipe2L": sprite(self.TilesSpritesheet.image_at((0,11*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),True),
            "pipe2R": sprite(self.TilesSpritesheet.image_at((16,11*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),True),
            "cloud1_1": sprite(self.TilesSpritesheet.image_at((0,20*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "cloud1_2": sprite(self.TilesSpritesheet.image_at((16,20*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "cloud1_3": sprite(self.TilesSpritesheet.image_at((32,20*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "cloud2_1": sprite(self.TilesSpritesheet.image_at((0,21*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "cloud2_2": sprite(self.TilesSpritesheet.image_at((16,21*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "cloud2_3": sprite(self.TilesSpritesheet.image_at((32,21*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "bush_1": sprite(self.TilesSpritesheet.image_at((11*16,11*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "bush_2": sprite(self.TilesSpritesheet.image_at((12*16,11*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False),
            "bush_3": sprite(self.TilesSpritesheet.image_at((13*16,11*16,16,16),2,colorkey=pygame.color.Color(0,0,0)),False)  
        }

    def getSprite(self,name):
        return self.backgroundSprites[name]

