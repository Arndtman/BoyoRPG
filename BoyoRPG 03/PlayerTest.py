import pygame
import time
import random
import BoyoRPG

#pygame.init()


class Player(object):
    def __init__(self, x, y, image, health=None):
        self.x = x
        self.y = y
        #AM 4/28/18 : moved velocity status
        self.x_vel = 0
        self.y_vel = 0
        self.health = 100
        self.image = image
        self.atk = False
        self.rotate = False
        self.invent = []
        
    def displayCharacter(self, swing):
        if swing:
            self.image = BoyoRPG.playerAtk
        else:
            self.image = BoyoRPG.player
        image2 = pygame.transform.flip(self.image, 1, 0)
        #JE 4/29: implemented advanced character animation
        if self.x_vel < 0: 
            self.rotate = True
            image2 = BoyoRPG.playerLstride
            if (self.x % 3   == 0):
                image2 =  BoyoRPG.playerLstride2
        elif self.x_vel  > 0:
            self.rotate = False
            self.image = BoyoRPG.playerRstride
            if (self.x % 3 == 0):
                self.image =  BoyoRPG.playerRstride2
            
        if self.rotate:
            BoyoRPG.gameDisplay.blit(image2, (self.x,self.y))
        else:
            BoyoRPG.gameDisplay.blit(self.image, (self.x,self.y))
        swing = False
        return swing

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        if self.x > BoyoRPG.display_width-9:
            self.x = self.x - 5
        if self.x < 0:
            self.x = 0
        if self.y > BoyoRPG.display_height - 10:
            self.y = self.y - 5
        if self.y < 0:
            self.y = 0

    def healthBar(self):
        hpColor = BoyoRPG.green
        if (self.health < 0):
            self.health = 0
            #boyorpg.restart()
        pygame.draw.rect(BoyoRPG.gameDisplay, BoyoRPG.black, (675, 520, 110, 35))
        pygame.draw.rect(BoyoRPG.gameDisplay, BoyoRPG.red, (680, 525, 100, 25))
        pygame.draw.rect(BoyoRPG.gameDisplay, hpColor, (680, 525, self.health, 25))
    
            
    def add2In(self, item):
        if len(self.invent) != 20:
            self.invent.append(item)

    def dropFIn(self, item):
        self.invent.remove(item)

    def getHealth(self):
        return self.health

    def getInvent(self):
        return self.invent


#class Mob(object):
#    def __init__(self, x, y, image, health=None, scale1=None):
#    def displayMob(self, xN):
#    def moveMob(self, xN, yN):


class World(object):
    def __init__(self, x, y, Map, button=None):
        self.x = x
        self.y = y
        self.Map = Map
        self.button = button
        
    def displayWorld(self):
        BoyoRPG.gameDisplay.blit(self.Map, (self.x,self.y))
        
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

    def mapLinks(self, x, y, width, height): #note lists
        for xarg, yarg, w, h in zip(x, y, width, height):
            print("xarg = ", xarg, "yarg = ", yarg, "w = ", w," h= ", h)
        
'''
class ItemObj(object):
    def __init__(self):

class Armor(ItemObj):
    def __init__(self, defense, image):
        super(Armor,ItemObj.__init__()
        self.defense = defense
        self.image = image
'''
