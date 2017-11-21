from Spritesheet import Spritesheet
import pygame
from pygame.color import Color
from Sprite import Sprite
from Animation import Animation


class Sprites():
    def __init__(self):
        self.CharacterSpritesheet = Spritesheet('img/characters.gif',16)
        self.TilesSpritesheet = Spritesheet('img/tiles.png',16)

        self.characterSprites = {
            "mario_idle": Sprite(self.CharacterSpritesheet.image_at(276, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_run1": Sprite(self.CharacterSpritesheet.image_at(290, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_run2": Sprite(self.CharacterSpritesheet.image_at(304, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_run3": Sprite(self.CharacterSpritesheet.image_at(321, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_break": Sprite(self.CharacterSpritesheet.image_at(337, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_jump": Sprite(self.CharacterSpritesheet.image_at(355, 44,2, colorkey=-1,ignoreTileSize=True),True)
        }

        self.animations = {
            "randomBox": Sprite(None,True,animation = Animation([self.TilesSpritesheet.image_at(24,0,2),self.TilesSpritesheet.image_at(25,0,2),self.TilesSpritesheet.image_at(26,0,2)]))
        }

        self.backgroundSprites = {
            "sky": Sprite(self.TilesSpritesheet.image_at(3,23,2),False),
            "bricks": Sprite(self.TilesSpritesheet.image_at(1,0,2),True),
            "ground": Sprite(self.TilesSpritesheet.image_at(0,0,2),True),
           
            "pipeL": Sprite(self.TilesSpritesheet.image_at(0,10,2),True),
            "pipeR": Sprite(self.TilesSpritesheet.image_at(1,10,2,colorkey=Color(0,0,0)),True),
            "pipe2L": Sprite(self.TilesSpritesheet.image_at(0,11,2,colorkey=Color(0,0,0)),True),
            "pipe2R": Sprite(self.TilesSpritesheet.image_at(1,11,2,colorkey=Color(0,0,0)),True),
           
            "cloud1_1": Sprite(self.TilesSpritesheet.image_at(0,20,2,colorkey=Color(0,0,0)),False),
            "cloud1_2": Sprite(self.TilesSpritesheet.image_at(1,20,2,colorkey=Color(0,0,0)),False),
            "cloud1_3": Sprite(self.TilesSpritesheet.image_at(2,20,2,colorkey=Color(0,0,0)),False),
            "cloud2_1": Sprite(self.TilesSpritesheet.image_at(0,21,2,colorkey=Color(0,0,0)),False),
            "cloud2_2": Sprite(self.TilesSpritesheet.image_at(1,21,2,colorkey=Color(0,0,0)),False),
            "cloud2_3": Sprite(self.TilesSpritesheet.image_at(2,21,2,colorkey=Color(0,0,0)),False),
           
            "bush_1": Sprite(self.TilesSpritesheet.image_at(11,11,2,colorkey=Color(0,0,0)),False),
            "bush_2": Sprite(self.TilesSpritesheet.image_at(12,11,2,colorkey=Color(0,0,0)),False),
            "bush_3": Sprite(self.TilesSpritesheet.image_at(13,11,2,colorkey=Color(0,0,0)),False),
        }


