from Spritesheet import Spritesheet
import pygame
from pygame.color import Color
from Sprite import Sprite
from Animation import Animation
import json
import pprint

class Sprites():
    def __init__(self):
        self.characterSprites = self.loadSprites("./sprites/CharacterSprites.json")
        self.animations = self.loadSprites("./sprites/AnimationSprites.json")
        self.backgroundSprites = self.loadSprites("./sprites/BackgroundSprites.json")

    def loadSprites(self,url):
        with open(url) as jsonData:
            data = json.load(jsonData)
            mySpritesheet = Spritesheet(data['spriteSheetURL'],16)
            dic = {}
            if(data['type'] == "background"):
                for sprite in data['sprites']:
                    try: 
                        colorkey = sprite['colorKey']
                    except KeyError:
                        colorkey = None
                    dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey),sprite['collision'],None,sprite['redrawBg'])
                return dic
            elif data['type'] == "animation":
                images = []
                for sprite in data['sprites']:
                    for image in sprite['images']:
                        images.append(mySpritesheet.image_at(image['x'],image['y'],image['scale']))
                    dic[sprite['name']] = Sprite(None,True,animation = Animation(images))
                return dic
            elif data['type'] == "character":
                for sprite in data['sprites']:
                    try: 
                        colorkey = sprite['colorKey']
                    except KeyError:
                        colorkey = None
                    dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey,True),sprite['collision'])
                return dic



            



