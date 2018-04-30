import pygame
import time
import random
import BoyoRPG

homeTown = BoyoRPG.pygame.image.load('png/hometown.png')
house1 = BoyoRPG.pygame.image.load('png/house1.png')
house2 = BoyoRPG.pygame.image.load('png/house2.png')
path2 = BoyoRPG.pygame.image.load('png/path2.png')
path3 = BoyoRPG.pygame.image.load('png/path3.png') 
bridge3 = BoyoRPG.pygame.image.load('png/bridge3.png')
forest1 = BoyoRPG.pygame.image.load('png/ForestMap1-Magdaleno.png')
sunkenChapel = BoyoRPG.pygame.image.load('png/SunkenChapel.png')
cliff = BoyoRPG.pygame.image.load('png/cliff.png')
lavaLake = BoyoRPG.pygame.image.load('png/Lava_Lake_MapAM.png')

homeTownbool = True
house1bool = False
house1Flipbool = False
path2bool = False
path3bool = False
house2bool = False
bridgebool = False
forestbool = False
sunkenChapelbool = False
cliffbool = False
lavaLakebool = False

#Unused, will be for restarting game
boolList = []
boolList.extend((homeTownbool, house1bool, house1Flipbool, path2bool,
                path3bool, house2bool, bridgebool, forestbool,
                sunkenChapelbool,cliffbool, lavaLakebool))


                

#Ideal case is as follows
##if homeTownbool:
##    boundaries(pInst, wInst)
##    mobs to spawn for this map, ensure they dont cross boundaries
##    if mob.Rect collides with pInst.Rect
##       p.Inst.health -= mob.attack
##    if pInst.attack.Rect collides with mob.Rect
##       mob.health -= pInst.attack
##    if in path2 bounds
##        go to path2 
##    if in house1 bounds + click 
##        go to house1                 
##    if in house2 bounds + click
##        go to house2
##if house2bool:
##    boundaries()
##    Blah

#THESE VALUES SHOULD PROBABLY NOT BE HERE FOR ANYTHING OTHER THAN TESTING
##display_width = 800
##display_height = 600 
blue = (0, 0, 255)
##black = (0, 0, 0)
##gameDisplay = pygame.display.set_mode((display_width, display_height))

#AM 4/29/2018: implemented collisions dictionary
rectDict = {}

#HOMETOWN
ht = []
rectDict['homeTown'] = ht
#house1
ht.append((105, 245, 120, 125))
#house1flip
ht.append((515, 240, 120, 125))
#townhall
ht.append((55, 5, 190, 210))
ht.append((535, 5, 215, 215))
ht.append((245, 5, 290, 135))

#HOUSE1FLIP
h1_f = []
rectDict['house1Flip'] = h1_f
h1_f.append((0, 0, 180, 270))
h1_f.append((0, 200, 25, 600))
h1_f.append((25, 350, 155, 170))
h1_f.append((0, 570, 800, 30))
h1_f.append((600, 435, 80, 110))
h1_f.append((755, 0, 45, 600))
h1_f.append((565, 35, 190, 65))
h1_f.append((180, 30, 310, 70))
h1_f.append((180, 95, 115, 30))
h1_f.append((410, 100, 75, 30))
h1_f.append((295, 240, 460, 195))
h1_f.append((490, 5, 70, 210))

#HOUSE1
h1 = []
rectDict['house1'] = h1
for wall in h1_f: # house1flip unflip
    h1.append((800 - wall[0] - wall[2], wall[1], wall[2], wall[3]))

#BRIDGE
brg = []
rectDict['bridge'] = brg
brg.append((275, 0, 230, 255))
brg.append((270, 315, 235, 280))
brg.append((520, 395, 210, 145))

#AM 4/29/18: wrote boundary collision function
def boundaries(pInst, wInst, key):
    futurePlayRect = pygame.Rect(pInst.x + pInst.x_vel/2, pInst.y + pInst.y_vel/2, 30, 35)
    list = rectDict[key]
    for rect_data in list:
        pygame.draw.rect(BoyoRPG.gameDisplay, blue, rect_data, 1)
        rect_data = (rect_data[0], rect_data[1], rect_data[2], rect_data[3] - 1 - 30 )
        rect = pygame.Rect(rect_data)
        if futurePlayRect.colliderect(rect):
            print("Collision at (", pInst.x, " ,", pInst.y, ") going ", pInst.x_vel, ", ", pInst.y_vel)
            if pInst.x + 29 < rect.left or pInst.x > rect.right - 1 :
                print("stop x velocity")
                pInst.x_vel = 0
            if pInst.y + 34 < rect.top:
                print("stop y velocity from the top")
                pInst.y_vel = 0
            if pInst.y - 1 > rect.bottom - 1:
                print("stop y velocity from the bottom")
                pInst.y_vel = 0
            print("l:", rect.left, " r:", rect.right, " u:", rect.top, "b:", rect.bottom)

def links(pInst, wInst):
    global path2bool
    global homeTownbool
    global bridgebool
    global forestbool
    global path3bool 
    global house2bool
    global house1bool
    global house1Flipbool
    global sunkenChapelbool
    global cliffbool
    global lavaLakebool

    click = BoyoRPG.pygame.mouse.get_pressed()
    
    currentmap = wInst.Map
    playRect = pygame.Rect(pInst.x, wInst.y, 30, 35)
    
    if homeTownbool:
        boundaries(pInst, wInst, 'homeTown')
        if 340 + 100 >= pInst.x >= 340 and 588 + 12 >= pInst.y >= 588:
            wInst.Map = path2
            pInst.x = 555
            pInst.y = 25
            path2bool = True
            homeTownbool = False
        if 140 + 30 >= pInst.x >= 140 and 340 + 15 > pInst.y >= 340 and click[0] == 1:
            wInst.Map = house1
            pInst.x = 245
            pInst.y = 465
            homeTownbool = False                
            house1bool = True  
        if 550 + 30 >= pInst.x >= 550 and 335 + 15 > pInst.y >= 335 and click[0] == 1:
            house1Flip = pygame.transform.flip(house1, 1, 0)
            wInst.Map = house1Flip
            pInst.x = 525
            pInst.y = 470
            homeTownbool = False
            house1Flipbool = True
    
    if house1bool:
        boundaries(pInst, wInst, 'house1')
        if 225 + 60 >= pInst.x >= 225 and 402 + 15 > pInst.y >= 402 and click[0] == 1:
          wInst.Map = homeTown
          pInst.x = 190
          pInst.y = 360
          house1bool = False
          homeTownbool = True
          
    if house1Flipbool:
        boundaries(pInst, wInst, 'house1Flip')
        if 510 + 50 >= pInst.x >= 510 and 402 + 15 > pInst.y >= 402 and click[0] == 1:
          wInst.Map = homeTown
          pInst.x = 535
          pInst.y = 345
          house1Flipbool = False
          homeTownbool = True

    if path2bool:
        if 533 + 60 > pInst.x > 510 and 0 + 3 > pInst.y >= 0:
            wInst.Map = homeTown
            pInst.x = 380
            pInst.y = 555
            path2bool = False
            homeTownbool = True
        if 0 + 12 > pInst.x >= 0 and 380 + 100 > pInst.y > 380:
            wInst.Map = bridge3
            pInst.x = 780
            pInst.y = 280
            path2bool = False
            bridgebool = True
        if 420 + 80 > pInst.x > 420 and 588 + 12 >= pInst.y >= 588:
            wInst.Map = path3
            pInst.x = 170
            pInst.y = 15
            path2bool = False
            path3bool = True
        if 235 > pInst.x > 0 and 220 > pInst.y > 0:
            pInst.x -= 5
            pInst.y -= 5
        if 520 + 230 > pInst.x > 520 and 50 + 220 > pInst.y > 50:
            pInst.x -= 5
            pInst.y -= 5

    if bridgebool:
        boundaries(pInst, wInst, 'bridge')
        if 780 + 20 > pInst.x > 780 and 240 + 60 > pInst.y > 240:
            wInst.Map = path2
            pInst.x = 15
            pInst.y = 430
            path2bool = True
            bridgebool = False
        if 0 + 15 > pInst.x >= 0 and 290 + 80 > pInst.y > 290:
            wInst.Map = forest1
            pInst.x = 770
            pInst.y = 270
            bridgebool = False
            forestbool = True
        if 700 + 80 >= pInst.x >= 700 and 0 + 10>= pInst.y >= 0:
            wInst.Map = cliff
            pInst.x = 625
            pInst.y = 530
            cliffbool = True
            bridgebool = False
            
    if cliffbool:
        if 500 + 260 >= pInst.x >= 500 and 580 + 20>= pInst.y >= 580:
            wInst.Map = bridge3
            pInst.x = 740
            pInst.y = 15
            cliffbool = False
            bridgebool = True
        if 640 + 35 >= pInst.x >= 635 and 70 + 20>= pInst.y >= 70:
            wInst.Map = lavaLake
            pInst.x = 765
            pInst.y = 480
            lavaLakebool = True
            cliffbool = False

    if lavaLakebool:
        if 780 + 20 >= pInst.x >= 780 and 430 + 80>= pInst.y >= 430:
            wInst.Map = cliff
            pInst.x = 655
            pInst.y = 110
            lavaLakebool = False
            cliffbool = True
    
            
    if forestbool:
        if 780 + 20 > pInst.x > 780 and 255 + 50 > pInst.y > 255:
            wInst.Map = bridge3
            pInst.x = 15
            pInst.y = 315
            bridgebool = True
            forestbool = False

    if path3bool:
        if 143 + 100 > pInst.x > 143 and 0 + 4 > pInst.y >= 0:
            wInst.Map = path2
            pInst.x = 450
            pInst.y = 580
            path2bool = True
            path3bool = False
        if 780 + 20 >= pInst.x >= 780 and 259 + 40>= pInst.y >= 259:
            wInst.Map = sunkenChapel
            pInst.x = 15 
            pInst.y = 105
            sunkenChapelbool = True
            path3bool = False
        if 70 + 35 >= pInst.x >= 70 and 259 + 20>= pInst.y >= 259 and click[0] == 1:
            wInst.Map = house2
            pInst.x = 700
            pInst.y = 415
            path3bool = False
            house2bool = True

    if house2bool:
        if 712 + 70 >= pInst.x >= 712 and 407 + 70 > pInst.y >= 407 and click[0] == 1:
            wInst.Map = path3
            pInst.x = 90
            pInst.y = 300
            path3bool = True
            house2bool = False

    if sunkenChapelbool:
        if 0 + 12 >= pInst.x >= 0 and 90 + 60>= pInst.y >= 90:
            wInst.Map = path3
            pInst.x = 760
            pInst.y = 290
            path3bool = True
            sunkenChapelbool = False

    
    if random.randint(0, 100) < 12:
        if wInst.Map != currentmap:
            BoyoRPG.loadScreen()
   # wInst.displayWorld()


def clear():
    global path2bool
    global homeTownbool
    global bridgebool
    global forestbool
    global path3bool 
    global house2bool
    global house1bool
    global house1Flipbool
    global sunkenChapelbool
    global cliffbool
    global lavaLakebool
    homeTownbool = True
    house1bool = False
    house1Flipbool = False
    path2bool = False
    path3bool = False
    house2bool = False
    bridgebool = False
    forestbool = False
    sunkenChapelbool = False
    cliffbool = False
    lavaLakebool = False
