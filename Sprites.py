from Spritesheet import Spritesheet
import pygame
from pygame.color import Color
from Sprite import Sprite
from Animation import Animation
import json
import pprint

class Sprites():
    def __init__(self):
        self.spriteCollection = self.loadSprites([  "./sprites/Mario.json",
                                                    "./sprites/Goomba.json",
                                                    "./sprites/AnimationSprites.json",
                                                    "./sprites/BackgroundSprites.json"])

    def loadSprites(self,urlList):
        resDict = {}
        for url in urlList:
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
                    resDict.update(dic)
                    continue
                elif data['type'] == "animation":
                    images = []
                    for sprite in data['sprites']:
                        for image in sprite['images']:
                            images.append(mySpritesheet.image_at(image['x'],image['y'],image['scale']))
                        dic[sprite['name']] = Sprite(None,True,animation = Animation(images))
                    resDict.update(dic)
                    continue
                elif data['type'] == "character":
                    for sprite in data['sprites']:
                        try: 
                            colorkey = sprite['colorKey']
                        except KeyError:
                            colorkey = None
                        dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey,True),sprite['collision'])
                    resDict.update(dic)
                    continue
        return resDict




            



