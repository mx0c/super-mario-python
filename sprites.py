from spritesheet import spritesheet
import pygame
from pygame.color import Color
from sprite import sprite
from animation import animation

class sprites():
    def __init__(self):
        self.CharacterSpritesheet = spritesheet('img/characters.gif',16)
        self.TilesSpritesheet = spritesheet('img/tiles.png',16)

        self.characterSprites = {
            "mario_idle": sprite(self.CharacterSpritesheet.image_at(276, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_run1": sprite(self.CharacterSpritesheet.image_at(290, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_run2": sprite(self.CharacterSpritesheet.image_at(304, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_run3": sprite(self.CharacterSpritesheet.image_at(321, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_break": sprite(self.CharacterSpritesheet.image_at(337, 44,2, colorkey=-1,ignoreTileSize=True),True),
            "mario_jump": sprite(self.CharacterSpritesheet.image_at(355, 44,2, colorkey=-1,ignoreTileSize=True),True)
        }

        self.animations = {
            "randomBox": sprite(None,True,animation = animation([self.TilesSpritesheet.image_at(24,0,2),self.TilesSpritesheet.image_at(25,0,2),self.TilesSpritesheet.image_at(26,0,2)]))
        }

        self.backgroundSprites = {
            "sky": sprite(self.TilesSpritesheet.image_at(3,23,2),False),
            "bricks": sprite(self.TilesSpritesheet.image_at(1,0,2),True),
            "ground": sprite(self.TilesSpritesheet.image_at(0,0,2),True),
           
            "pipeL": sprite(self.TilesSpritesheet.image_at(0,10,2),True),
            "pipeR": sprite(self.TilesSpritesheet.image_at(1,10,2,colorkey=Color(0,0,0)),True),
            "pipe2L": sprite(self.TilesSpritesheet.image_at(0,11,2,colorkey=Color(0,0,0)),True),
            "pipe2R": sprite(self.TilesSpritesheet.image_at(1,11,2,colorkey=Color(0,0,0)),True),
           
            "cloud1_1": sprite(self.TilesSpritesheet.image_at(0,20,2,colorkey=Color(0,0,0)),False),
            "cloud1_2": sprite(self.TilesSpritesheet.image_at(1,20,2,colorkey=Color(0,0,0)),False),
            "cloud1_3": sprite(self.TilesSpritesheet.image_at(2,20,2,colorkey=Color(0,0,0)),False),
            "cloud2_1": sprite(self.TilesSpritesheet.image_at(0,21,2,colorkey=Color(0,0,0)),False),
            "cloud2_2": sprite(self.TilesSpritesheet.image_at(1,21,2,colorkey=Color(0,0,0)),False),
            "cloud2_3": sprite(self.TilesSpritesheet.image_at(2,21,2,colorkey=Color(0,0,0)),False),
           
            "bush_1": sprite(self.TilesSpritesheet.image_at(11,11,2,colorkey=Color(0,0,0)),False),
            "bush_2": sprite(self.TilesSpritesheet.image_at(12,11,2,colorkey=Color(0,0,0)),False),
            "bush_3": sprite(self.TilesSpritesheet.image_at(13,11,2,colorkey=Color(0,0,0)),False),
        }


