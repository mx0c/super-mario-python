from sprites import sprites

class drawLevel():
    def __init__(self):
        self.sprites = sprites()
        self.level = [
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,6,7,8,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,0,0,0,0,9,10,11,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,4,5,0,0,0,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,1,1,1,1,1]
                ]
    
    def drawLevel(self,screen):

        for x in range(0,20):
            for y in range(0,15):
                dimensions = (x*32,y*32)
                if(self.level[y][x] == 0):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                elif(self.level[y][x] == 1):
                    screen.blit(self.sprites.backgroundSprites["ground"].image,dimensions)
                elif(self.level[y][x] == 2):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["pipeL"].image,dimensions)
                elif(self.level[y][x] == 3):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["pipeL"].image,dimensions)
                elif(self.level[y][x] == 4):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["pipe2L"].image,dimensions)
                elif(self.level[y][x] == 5):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["pipe2R"].image,dimensions)
                elif(self.level[y][x] == 6):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["cloud1_1"].image,dimensions)
                elif(self.level[y][x] == 7):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["cloud1_2"].image,dimensions)
                elif(self.level[y][x] == 8):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["cloud1_3"].image,dimensions)
                elif(self.level[y][x] == 9):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["cloud2_1"].image,dimensions)
                elif(self.level[y][x] == 10):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["cloud2_2"].image,dimensions)
                elif(self.level[y][x] == 11):
                    screen.blit(self.sprites.backgroundSprites["sky"].image,dimensions)
                    screen.blit(self.sprites.backgroundSprites["cloud2_3"].image,dimensions)
