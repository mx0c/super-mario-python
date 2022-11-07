import pygame
import sys
import json

from classes.Sprites import Sprites


def loadBlocks():
    with open("./sprites/BackgroundSprites.json", "r") as file:
        data = json.load(file)

    # gets the names of background sprites
    blocks = [data["sprites"][i]["name"] for i in range(len(data["sprites"]))]

    translatedBlocks = []
    for block in blocks:
        translatedBlock = block.translate(
            str.maketrans({"R": "", "L": "", "_": "", "1": "", "2": "", "3": ""})
        )
        if translatedBlock not in translatedBlocks:
            translatedBlocks.append(translatedBlock)

    return translatedBlocks


def drawLines():
    for i in range(HEIGHT // cellSize):  # Drawing lines verticaly
        pygame.draw.line(screen, white, (cellSize * i, 0), (cellSize * i, WIDTH), 1)

    for i in range(WIDTH // cellSize):  # Drawing lines horizontaly
        pygame.draw.line(screen, white, (0, cellSize * i), (HEIGHT, cellSize * i), 1)


def drawCloudSprite():
    for yOff in range(0, 2):
        for xOff in range(0, 3):
            screen.blit(
                Sprites()
                .spriteCollection.get("cloud{}_{}".format(yOff + 1, xOff + 1))
                .image,
                ((gridLocationX + xOff) * cellSize, (gridLocationY + yOff) * cellSize),
            )


def drawPipeSprite():
    placedBlocks[currentBlock][-1].append(0)

    screen.blit(
        Sprites().spriteCollection.get("pipeL").image,
        (gridLocationX * cellSize, gridLocationY * cellSize),
    )
    screen.blit(
        Sprites().spriteCollection.get("pipeR").image,
        ((gridLocationX + 1) * cellSize, gridLocationY * cellSize),
    )

    for i in range(1, (HEIGHT // cellSize) - gridLocationY):
        screen.blit(
            Sprites().spriteCollection.get("pipe2L").image,
            (gridLocationX * cellSize, (gridLocationY + i) * cellSize),
        )
    for i in range(1, (HEIGHT // cellSize) - gridLocationY):
        screen.blit(
            Sprites().spriteCollection.get("pipe2R").image,
            ((gridLocationX + 1) * cellSize, (gridLocationY + i) * cellSize),
        )


def drawBushSprite():
    for xOff in range(3):
        screen.blit(
            Sprites().spriteCollection.get("bush_{}".format(xOff + 1)).image,
            ((gridLocationX + xOff) * cellSize, gridLocationY * cellSize),
        )


def drawSprite():
    global gridLocationX, gridLocationY

    mouseX, mouseY = pygame.mouse.get_pos()
    gridLocationX, gridLocationY = mouseX // cellSize, mouseY // cellSize

    placedBlocks[currentBlock] = placedBlocks.get(currentBlock, [])
    placedBlocks[currentBlock].append([gridLocationX, gridLocationY])

    if currentBlock == "cloud":
        drawCloudSprite()
    elif currentBlock == "pipe":
        drawPipeSprite()
    elif currentBlock == "bush":
        drawBushSprite()
    else:
        screen.blit(
            Sprites().spriteCollection.get(currentBlock).image,
            (gridLocationX * cellSize, gridLocationY * cellSize),
        )


def createJsonFile():
    try:
        jsonData = {
            "id": 2,
            "length": 20,
            "level": {
                "objects": {
                    "bush": placedBlocks["bush"],
                    "sky": placedBlocks["sky"],
                    "cloud": placedBlocks["cloud"],
                    "pipe": placedBlocks["pipe"],
                    "ground": placedBlocks["ground"],
                },
                "layers": {
                    "sky": {"x": [0, 60], "y": [0, 13]},
                    "ground": {"x": [0, 60], "y": [14, 16]},
                },
            },
        }

        with open("./levels/Level1-3.json", "w") as file:
            json.dump(jsonData, file, indent=4)

    except:
        blocksNotPlaced = []
        for block in blocks:
            if block not in placedBlocks:
                blocksNotPlaced.append(block)
        print(
            "Missing blocks {} place them to save the json file".format(blocksNotPlaced)
        )


def changeBlock():
    global currentBlock
    currentBlockIndex = blocks.index(currentBlock)

    # Cycle through the blocks if reached the end then start again from the start
    if currentBlockIndex < len(blocks) - 1:
        currentBlock = blocks[currentBlockIndex + 1]
    else:
        currentBlock = blocks[0]
    print("Current Block: {}".format(currentBlock))


def keyPressed():
    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    if pressedKeys[pygame.K_TAB]:
        changeBlock()

    if pressedKeys[pygame.K_s]:
        createJsonFile()


# GLOBAL VARIABLES
HEIGHT, WIDTH = 640, 480
cellSize = 32

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Level Editor")

white = (255, 255, 255)

blocks = loadBlocks()
currentBlock = blocks[0]
placedBlocks = {}

gridLocationX, gridLocationY = 0, 0

print("Current Block: {}".format(currentBlock))


def main():
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                keyPressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawSprite()

        drawLines()
        pygame.display.update()


if __name__ == "__main__":
    main()
