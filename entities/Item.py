from entities.EntityBase import EntityBase
from classes.Animation import Animation
import pygame
from copy import copy
from classes.Maths import vec2D
from classes.Sound import Sound
from classes.Dashboard import Dashboard

class Item(Dashboard):
    def __init__(self,collection,screen,x,y):
        super(Item,self).__init__("./img/font.png",8,screen)
        self.ItemPos = vec2D(x,y) 
        self.itemVel = vec2D(0,0)
        self.screen = screen
        self.coin_animation = copy(collection.get('coin-item').animation)
        self.sound_played = False
        
    def spawnCoin(self,cam,sound,dashboard):
        if(not self.sound_played):
            self.sound_played = True
            dashboard.points+=100
            sound.play_sfx(sound.coin)
        self.coin_animation.update()
        if(self.coin_animation.timer < 45):
            if(self.coin_animation.timer < 15):
                self.itemVel.y-=0.5
                self.ItemPos.y += self.itemVel.y
            elif(self.coin_animation.timer < 45):
                self.itemVel.y+=0.5
                self.ItemPos.y += self.itemVel.y
            self.screen.blit(self.coin_animation.image,(self.ItemPos.x+cam.pos.x*32,self.ItemPos.y))
            self.drawText("100",self.ItemPos.x+18+cam.pos.x*32,self.ItemPos.y+4,8)
