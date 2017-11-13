from sprites import sprites

class drawLevel():
    def __init__(self):
        self.sprites = sprites()
        self.getLineOfSprites = lambda x: [(self.sprites.getSprite(x)) for i in range(20)]
        self.level = [
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("sky"),
                    self.getLineOfSprites("ground"),
                    self.getLineOfSprites("ground")
                ]
        self.addCloudSprite(5,5)
        self.addCloudSprite(13,3)
        self.addPipeSprite(8,10)
        self.addPipeSprite(10,12)
    
    def drawLevel(self,screen):
        for x in range(0,20):
            for y in range(0,15):
                dimensions = (x*32,y*32)
                screen.blit(self.sprites.getSprite("sky").image,dimensions)
                screen.blit(self.level[y][x].image,dimensions)

    #TODO: Refactor
    def addCloudSprite(self,x,y):
        self.level[y][x] = self.sprites.getSprite("cloud1_1")
        self.level[y][x+1] = self.sprites.getSprite("cloud1_2")
        self.level[y][x+2] = self.sprites.getSprite("cloud1_3")
        self.level[y+1][x] = self.sprites.getSprite("cloud2_1") 
        self.level[y+1][x+1] = self.sprites.getSprite("cloud2_2")
        self.level[y+1][x+2] = self.sprites.getSprite("cloud2_3")

    def addPipeSprite(self,x,y):
        self.level[y][x] = self.sprites.getSprite("pipeL")
        self.level[y][x+1] = self.sprites.getSprite("pipeR")
        self.level[y+1][x] = self.sprites.getSprite("pipe2L")
        self.level[y+1][x+1] = self.sprites.getSprite("pipe2R")
        self.level[y+2][x] = self.sprites.getSprite("pipe2L")
        self.level[y+2][x+1] = self.sprites.getSprite("pipe2R")