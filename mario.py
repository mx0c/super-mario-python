import sprites

class mario():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = {x:0,y:0}
		
    def drawMario(self):
        sprites.screen.blit(sprites.mario,(self.x*32,self.y*32))
	
    def updateMario(self):
        pass
