import pygame
import time
import random
import BoyoRPG

#pygame.init()


class Player(object):
    def __init__(self, x, y, image, health=None):
        self.x = x
        self.y = y
        self.health = health
        self.image = image
        self.rotate = False
        
    def displayCharacter(self, xN):
        image2 = pygame.transform.flip(self.image, 1, 0)
        if xN < 0: 
            self.rotate = True
        elif xN > 0:
            self.rotate = False
        if self.rotate:
            BoyoRPG.gameDisplay.blit(image2, (self.x,self.y))
        else:
            BoyoRPG.gameDisplay.blit(self.image, (self.x,self.y))

    def move(self, xN, yN):
        self.x += xN
        self.y += yN
        if self.x > BoyoRPG.display_width-9:
            self.x = self.x - 5
        if self.x < 0:
            self.x = 0
        if self.y > BoyoRPG.display_height - 10:
            self.y = self.y - 5
        if self.y < 0:
            self.y = 0

            
        
#class Mob(object):
#    def __init__(self, x, y, image, health=None, scale1=None):
#    def displayMob(self, xN):
#    def moveMob(self, xN, yN):


class World(object):
    def __init__(self, x, y, image, button=None):
        self.x = x
        self.y = y
        self.image = image
        self.button = button
        
    def displayWorld(self):
        BoyoRPG.gameDisplay.blit(self.image, (self.x,self.y))
        
    def makeWorld(self, x1):
        self.displayWorld()
        #print(x1)
        
    def button(self, x, y, w, h, px, py, action, *args):
        mouse = BoyoRPG.pygame.mouse.get_pos()
        click = BoyoRPG.pygame.mouse.get_pressed()
        #global enter
    
        if x + w > px > x and y + h > py > y:
            print('almost') 
            if click[0] == 1 and action != None:
                print('yea')
                #enter = not enter
                action(*args) #runs object as function
        else:
            print('no')

