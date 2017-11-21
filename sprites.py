from Spritesheet import Spritesheet
import pygame
from pygame.color import Color
from Sprite import Sprite
from Animation import Animation
import json
import pprint

class Sprites():
    def __init__(self):
        self.characterSprites = self.loadSprites("./sprites/CharacterSprites.json","character")
        self.animations = self.loadSprites("./sprites/AnimationSprites.json","animation")
        self.backgroundSprites = self.loadSprites("./sprites/BackgroundSprites.json","background")

    def loadSprites(self,url, type):
        with open(url) as jsonData:
            data = json.load(jsonData)
            mySpritesheet = Spritesheet(data['spriteSheetURL'],16)
            dic = {}
            if(type is "background"):
                for sprite in data['sprites']:
                    try: 
                        colorkey = sprite['colorKey']
                    except KeyError:
                        colorkey = None
                    dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey),sprite['collision'])
                return dic
            elif type is "animation":
                images = []
                for sprite in data['sprites']:
                    for image in sprite['images']:
                        images.append(mySpritesheet.image_at(image['x'],image['y'],image['scale']))
                    dic[sprite['name']] = Sprite(None,True,animation = Animation(images))
                return dic
            elif type is "character":
                for sprite in data['sprites']:
                    try: 
                        colorkey = sprite['colorKey']
                    except KeyError:
                        colorkey = None
                    dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey,True),sprite['collision'])
                return dic



            



