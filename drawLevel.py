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
                if(self.level[y][x] == 0):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                elif(self.level[y][x] == 1):
                    screen.blit(self.sprites.ground,(x*32,y*32))
                elif(self.level[y][x] == 2):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.pipeL,(x*32,y*32))
                elif(self.level[y][x] == 3):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.pipeR,(x*32,y*32))
                elif(self.level[y][x] == 4):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.pipe2L,(x*32,y*32))
                elif(self.level[y][x] == 5):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.pipe2R,(x*32,y*32))
                elif(self.level[y][x] == 6):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.cloud1_1,(x*32,y*32))
                elif(self.level[y][x] == 7):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.cloud1_2,(x*32,y*32))
                elif(self.level[y][x] == 8):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.cloud1_3,(x*32,y*32))
                elif(self.level[y][x] == 9):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.cloud2_1,(x*32,y*32))
                elif(self.level[y][x] == 10):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.cloud2_2,(x*32,y*32))
                elif(self.level[y][x] == 11):
                    screen.blit(self.sprites.sky,(x*32,y*32))
                    screen.blit(self.sprites.cloud2_3,(x*32,y*32))
