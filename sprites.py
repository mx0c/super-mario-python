import spritesheet as sprite
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

CharacterSpritesheet = sprite.spritesheet('img/characters.gif',16)
TilesSpritesheet = sprite.spritesheet('img/tiles.png',16)

mario = CharacterSpritesheet.image_at((276, 44, 16, 16),4)
sky = TilesSpritesheet.image_at((48, 368, 16, 16),2)
bricks = TilesSpritesheet.image_at((16,0,16,16),2)
ground = TilesSpritesheet.image_at((0,0,16,16),2)
