import json
import pygame

from classes.Sprites import Sprites
from classes.Tile import Tile
from entities.Coin import Coin
from entities.CoinBrick import CoinBrick
from entities.Goomba import Goomba
from entities.Mushroom import RedMushroom
from entities.Koopa import Koopa
from entities.CoinBox import CoinBox
from entities.RandomBox import RandomBox
from entities.CompositeEntity import CompositeEntity  # Import CompositeEntity

#new classes needed for win condition implementation
from classes.Observer import Subject
from entities.EndGoal import Goal

#level class is now a subject for the observer design pattern
class Level(Subject):
    def _init_(self, screen, sound, dashboard):
        Subject._init_(self)
        self.sprites = Sprites()
        self.dashboard = dashboard
        self.sound = sound
        self.screen = screen
        self.level = None
        self.levelLength = 0
        self.entityList = CompositeEntity()  # Use CompositeEntity to manage all entities

        #added for the win condition implemetation
        self.currentLevelName = ""
        self.completed_levels = set() 

    def loadLevel(self, levelname):
        self.currentLevelName = levelname
        
        with open("./levels/{}.json".format(levelname)) as jsonData:
            data = json.load(jsonData)
            self.loadLayers(data)
            self.loadObjects(data)
            self.loadEntities(data)
            self.levelLength = data["length"]

            #added for win condition implementation
            goal_x = self.levelLength - 2  
            self.addGoal(goal_x, 8)

    def loadEntities(self, data):
        try:
           # Use CompositeEntity to group entities together
            coin_box_group = CompositeEntity()
            goomba_group = CompositeEntity()
            koopa_group = CompositeEntity()
            coin_group = CompositeEntity()
            coin_brick_group = CompositeEntity()
            random_box_group = CompositeEntity()

            [coin_box_group.add(self.addCoinBox(x, y)) for x, y in data["level"]["entities"]["CoinBox"]]
            [goomba_group.add(self.addGoomba(x, y)) for x, y in data["level"]["entities"]["Goomba"]]
            [koopa_group.add(self.addKoopa(x, y)) for x, y in data["level"]["entities"]["Koopa"]]
            [coin_group.add(self.addCoin(x, y)) for x, y in data["level"]["entities"]["coin"]]
            [coin_brick_group.add(self.addCoinBrick(x, y)) for x, y in data["level"]["entities"]["coinBrick"]]
            [random_box_group.add(self.addRandomBox(x, y, item)) for x, y, item in data["level"]["entities"]["RandomBox"]]

            # Now add the groups to the main entity list
            self.entityList.add(coin_box_group)
            self.entityList.add(goomba_group)
            self.entityList.add(koopa_group)
            self.entityList.add(coin_group)
            self.entityList.add(coin_brick_group)
            self.entityList.add(random_box_group)
        except:
            # if no entities in Level
            pass

    def loadLayers(self, data):
        layers = []
        for x in range(*data["level"]["layers"]["sky"]["x"]):
            layers.append(
                (
                        [
                            Tile(self.sprites.spriteCollection.get("sky"), None)
                            for y in range(*data["level"]["layers"]["sky"]["y"])
                        ]
                        + [
                            Tile(
                                self.sprites.spriteCollection.get("ground"),
                                pygame.Rect(x * 32, (y - 1) * 32, 32, 32),
                            )
                            for y in range(*data["level"]["layers"]["ground"]["y"])
                        ]
                )
            )
        self.level = list(map(list, zip(*layers)))

    def loadObjects(self, data):
        for x, y in data["level"]["objects"]["bush"]:
            self.addBushSprite(x, y)
        for x, y in data["level"]["objects"]["cloud"]:
            self.addCloudSprite(x, y)
        for x, y, z in data["level"]["objects"]["pipe"]:
            self.addPipeSprite(x, y, z)
        for x, y in data["level"]["objects"]["sky"]:
            self.level[y][x] = Tile(self.sprites.spriteCollection.get("sky"), None)
        for x, y in data["level"]["objects"]["ground"]:
            self.level[y][x] = Tile(
                self.sprites.spriteCollection.get("ground"),
                pygame.Rect(x * 32, y * 32, 32, 32),
            )

   
    def updateEntities(self, cam):
         for entity in list(self.entityList.entities):  # Convert to list to avoid modifying during iteration
            entity.update(cam)
            if hasattr(entity, "alive") and not entity.alive:
              self.entityList.remove(entity)

    def drawLevel(self, camera):
        try:
            for y in range(0, 15):
                for x in range(0 - int(camera.pos.x + 1), 20 - int(camera.pos.x - 1)):
                    if self.level[y][x].sprite is not None:
                        if self.level[y][x].sprite.redrawBackground:
                            self.screen.blit(
                                self.sprites.spriteCollection.get("sky").image,
                                ((x + camera.pos.x) * 32, y * 32),
                            )
                        self.level[y][x].sprite.drawSprite(
                            x + camera.pos.x, y, self.screen
                        )
            self.updateEntities(camera)
        except IndexError:
            return

    def addCloudSprite(self, x, y):
        try:
            for yOff in range(0, 2):
                for xOff in range(0, 3):
                    self.level[y + yOff][x + xOff] = Tile(
                        self.sprites.spriteCollection.get("cloud{}_{}".format(yOff + 1, xOff + 1)), None, )
        except IndexError:
            return

    def addPipeSprite(self, x, y, length=2):
        try:
            # add pipe head
            self.level[y][x] = Tile(
                self.sprites.spriteCollection.get("pipeL"),
                pygame.Rect(x * 32, y * 32, 32, 32),
            )
            self.level[y][x + 1] = Tile(
                self.sprites.spriteCollection.get("pipeR"),
                pygame.Rect((x + 1) * 32, y * 32, 32, 32),
            )
            # add pipe body
            for i in range(1, length + 20):
                self.level[y + i][x] = Tile(
                    self.sprites.spriteCollection.get("pipe2L"),
                    pygame.Rect(x * 32, (y + i) * 32, 32, 32),
                )
                self.level[y + i][x + 1] = Tile(
                    self.sprites.spriteCollection.get("pipe2R"),
                    pygame.Rect((x + 1) * 32, (y + i) * 32, 32, 32),
                )
        except IndexError:
            return

    def addBushSprite(self, x, y):
        try:
            self.level[y][x] = Tile(self.sprites.spriteCollection.get("bush_1"), None)
            self.level[y][x + 1] = Tile(
                self.sprites.spriteCollection.get("bush_2"), None
            )
            self.level[y][x + 2] = Tile(
                self.sprites.spriteCollection.get("bush_3"), None
            )
        except IndexError:
            return

    def addCoinBox(self, x, y):
        self.level[y][x] = Tile(None, pygame.Rect(x * 32, y * 32 - 1, 32, 32))
        coin_box = CoinBox(
        self.screen, self.sprites.spriteCollection, x, y, self.sound, self.dashboard
    )
        self.entityList.add(coin_box)
        return coin_box 

    def addRandomBox(self, x, y, item):
        self.level[y][x] = Tile(None, pygame.Rect(x * 32, y * 32 - 1, 32, 32))
        random_box = RandomBox(
        self.screen, self.sprites.spriteCollection, x, y, item, self.sound, self.dashboard, self
    )
        self.entityList.add(random_box)
        return random_box  # Return instance

    def addCoin(self, x, y):
        coin = Coin(self.screen, self.sprites.spriteCollection, x, y)
        self.entityList.add(coin)
        return coin

    def addCoinBrick(self, x, y):
        self.level[y][x] = Tile(None, pygame.Rect(x * 32, y * 32 - 1, 32, 32))
        coin_brick = CoinBrick(
                self.screen,
                self.sprites.spriteCollection,
                x,
                y,
                self.sound,
                self.dashboard
            )
        self.entityList.add(coin_brick)
        return coin_brick
        

    def addGoomba(self, x, y):
        goomba= Goomba(self.screen, self.sprites.spriteCollection, x, y, self, self.sound)
        self.entityList.add(goomba)
        return goomba

    def addKoopa(self, x, y):
        koopa = Koopa(self.screen, self.sprites.spriteCollection, x, y, self, self.sound)
        self.entityList.add(koopa)
        return koopa

    def addRedMushroom(self, x, y):
        mushroom = RedMushroom(self.screen, self.sprites.spriteCollection, x, y, self, self.sound)
        self.entityList.add(mushroom)
        return mushroom

    
    
    #added for win condition implementation
    def addGoal(self, x, y):
        #add flag to the level end point to show where the goal is
        goal = Goal(self.screen, self.sprites.spriteCollection, x, y, self)
        self.entityList.add(goal)
        return goal

    def mark_level_complete(self):
        #add the current level to completed levels
        self.completed_levels.add(self.currentLevelName)
        #need to notify observers about level completion
        self.notify_observers("level_complete", level_name=self.currentLevelName)
        
    def is_level_completed(self, level_name):
        return level_name in self.completed_levels