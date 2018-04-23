import pygame
import time
import random
import ctypes
from tkinter import *
#from PlayerTest import *

#########AA 4/16 added a lot of stuff #######

#Message box below
#Sound: theme/swing
#Linkage between maps
#Global Boolean's
#pygame image Globals
#Health bar on bottom right

App = Tk()
App.title('Message Box');

Message (App, text = "\t\tMessage Box\n"

         "\n"

         "Welcome: This is a test dialogue box and stuff. \n"
         "Movement: WASD \n"
         "Attacks: Left Mouse \n"
         "Enter Houses: Left Mouse \n \n"
         "Every Path and House will take you somewhere!\n"
         "(except for homeTown castle) :( \n"
         "yes I know the swing sound is very buggy\n\n"
         "Report any bugs as there are some movement/animation ones, \n"
         "but try to exit the game and recreate them first\n\n"
         "Hit that RED [X] on top right to start the game! \n",
         fg = "blue", bg = "powder blue", bd = 20,
         relief = GROOVE, font=('arial', 20, 'bold')).pack(padx=10, pady=10)
App.mainloop()

pygame.init()
pygame.display.set_caption('Boyo RPG')
clock = pygame.time.Clock()

pygame.mixer.music.load("MM.wav")
MMInto = pygame.image.load('MM.png')
pygame.mixer.music.play(-1) #-1 loop, 1= play 1 + 1, 5=6plays

swing = pygame.mixer.Sound('swing.wav')
swing.set_volume(0.4)

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (197, 179, 88)
#offset colors for menu flare
bgreen = (25, 209, 47) 
bred = (255, 114, 92)
bblue = (0, 0, 139)

pause = False

enter = False

attack = False

rotate = True

homeTown = pygame.image.load('hometown.png')
house1 = pygame.image.load('house1.png')
house2 = pygame.image.load('house2.png') 
path2 = pygame.image.load('path2.png')
path3 = pygame.image.load('path3.png') 
bridge3 = pygame.image.load('bridge3.png')
forest1 = pygame.image.load('ForestMap1-Magdaleno.png')
sunkenChapel = pygame.image.load('SunkenChapel.png')
cliff = pygame.image.load('cliff.png')
lavaLake = pygame.image.load('Lava_Lake_MapAM.png') 
player = pygame.image.load('knight1.png')
playerAtk = pygame.image.load('knight2.png')
att = pygame.image.load('att.png')

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

gameDisplay = pygame.display.set_mode((display_width, display_height))


def quitGame():
    pygame.quit()
    quit()


def healthBar(hp):
    hpColor = blue
    if hp < 30:
        hpColor = red
    pygame.draw.rect(gameDisplay, hpColor, (680, 525, hp, 25))

def character(chara, x,y, atk):
    global att
    gameDisplay.blit(chara, (x,y))
    if atk:
        if rotate:
            gameDisplay.blit(att, (x + 40, y + 10 ))
        else:
            gameDisplay.blit(att, (x - 45, y + 10))

#returns a manipulatable COLOR-ed rectangle
#with TEXT written on it.
#used for button creation
#Very generic
def text_objects(text, font, color=None):
    if color == None:
        color = black
    textSurface = font.render(text, True, color) #true is anti-alaisng
    return textSurface, textSurface.get_rect() 

#button(155, 340, 25, 30, x, y, game_loop, house, player_h1, 0, 0, 50, 300)

def button(x, y, w, h, px, py, action=None, *args): #action=None
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global enter

    if x + w > px > x and y + h > py > y:
        print('almost (click to enter)')
        if click[0] == 1 and action != None:
            #print('click to enter')
            enter = not enter
            action(*args) #runs object as function
    #else:
        #print('no')

def button_mm(msg, x, y, w, h, c1, c2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)
    #print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, c2, (x, y, w, h))
        if click[0] == 1 and action != None :
            action() #runs object as function
    else:
        pygame.draw.rect(gameDisplay, c1, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def world(Map, chara ,mx, my, px, py):
    gameDisplay.blit(Map, (mx, my))
    character(chara, px,py)

#experimental
def game_intro():
    intro = True
    pygame.mixer.music.play(-1) #-1 loop, 1= play 1 + 1, 5=6plays
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(MMInto, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("BoYo RpG", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


        button_mm("Play Beta",250, 350, 100, 50, green, bgreen, game_loop,
               homeTown, player, 0, 0, 380, 555, 100)
        #pass game_loop object
        button_mm("Quit Beta", 350, 350, 200, 50, red, bred, quitGame)
        mouse = pygame.mouse.get_pos()
        #print(mouse)

        pygame.display.update()
        clock.tick(15)



def game_loop(Map, chara, mx, my, px, py, health):
    global pause
    global enter
    global attack
    global playerAtk
    global player
    global rotate
    #AA 4/16
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
    x = px
    y = py
    x_pos = 0
    y_pos = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #exit key
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #left arrow
                    x_pos = -5
                if event.key == pygame.K_d:
                    x_pos = 5
                if event.key == pygame.K_w: #left arrow
                    y_pos = -5
                if event.key == pygame.K_s:
                    y_pos = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_pos = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_pos = 0

#AA 4/16
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            attack = True
        #print(rotate)
        if health < 0:
            quitGame()
#AA 4/16
        if attack:
            swing.play()
            chara = playerAtk;
        else:
            chara = player;

        x += x_pos
        y += y_pos


        if x > display_width-9:
            x = x - 5
        if x < 0:
            x = 0
        if y > display_height - 10:
            y = y - 5
        if y < 0:
            y = 0
    
        print("x = ", x, "y = ", y) 
        #idea for map truth dictionary Note: much faster/efficient than comprehesion/recursion
        #    for inner in dict_data.values():
        #      for key in inner:
        #        if key != to the one we want 
        #           inner[key] = 0 (set to false)
        #        if key = to the one we want
        #           inner[key] = 1 (set to true)

        #print("PATH3 BOOL = " + str(path3bool), "X = " , x , " Y = " , y)
        #print("PATH2 BOOL = " + str(path2bool), "X = " , x , " Y = " , y)
#AA 4/16
        if homeTownbool:
            if 340 + 100 >= x >= 340 and 588 + 12 >= y >= 588:
                Map = path2
                x = 555
                y = 24
                path2bool = True
                homeTownbool = False
            if 140 + 30 >= x >= 140 and 340 + 15 > y >= 340 and click[0] == 1:
                Map = house1
                x = 245
                y = 462
                homeTownbool = False                
                house1bool = True  
            if 550 + 30 >= x >= 550 and 335 + 15 > y >= 335 and click[0] == 1:
                house1Flip = pygame.transform.flip(house1, 1, 0)
                Map = house1Flip
                x = 525
                y = 470
                homeTownbool = False
                house1Flipbool = True

        if house1bool:
            if 225 + 60 >= x >= 225 and 402 + 15 > y >= 402 and click[0] == 1:
              Map = homeTown
              x = 190
              y = 360
              house1bool = False
              homeTownbool = True

        if house1Flipbool:
            if 510 + 50 >= x >= 510 and 402 + 15 > y >= 402 and click[0] == 1:
              Map = homeTown
              x = 535
              y = 345
              house1Flipbool = False
              homeTownbool = True

        if path2bool:
            if 533 + 60 > x > 510 and 0 + 3 > y >= 0:
                Map = homeTown
                x = 380
                y = 555
                path2bool = False
                homeTownbool = True
            if 0 + 12 > x >= 0 and 380 + 100 > y > 380:
                Map = bridge3
                x = 780
                y = 280
                path2bool = False
                bridgebool = True
            if 420 + 80 > x > 420 and 588 + 12 >= y >= 588:
                Map = path3
                x = 170
                y = 14
                path2bool = False
                path3bool = True
            if 235 >= x >= 0 and 220 >= y >= 0:
                x -= x_pos
                y -= y_pos
            if 520 + 230 >= x >= 520 and 50 + 220 >= y >= 50:
                x -= x_pos
                y -= y_pos

        if bridgebool:
            if 780 + 20 > x > 780 and 240 + 60 > y > 240:
                Map = path2
                x = 13
                y = 428
                path2bool = True
                bridgebool = False
            if 0 + 15 > x >= 0 and 290 + 80 > y > 290:
                Map = forest1
                x = 770
                y = 270
                bridgebool = False
                forestbool = True
            if 700 + 80 >= x >= 700 and 0 + 10>= y >= 0:
                Map = cliff
                x = 625
                y = 530
                cliffbool = True
                bridgebool = False
                
        if cliffbool:
            if 500 + 260 >= x >= 500 and 580 + 20>= y >= 580:
                Map = bridge3
                x = 740
                y = 15
                cliffbool = False
                bridgebool = True
            if 640 + 35 >= x >= 635 and 70 + 20>= y >= 70:
                Map = lavaLake
                x = 765
                y = 480
                lavaLakebool = True
                cliffbool = False

        if lavaLakebool:
            if 780 + 20 >= x >= 780 and 430 + 80>= y >= 430:
                Map = cliff
                x = 655
                y = 110
                lavaLakebool = False
                cliffbool = True
        
                
        if forestbool:
            if 780 + 20 > x > 780 and 255 + 50 > y > 255:
                Map = bridge3
                x = 14
                y = 313
                bridgebool = True
                forestbool = False

        if path3bool:
            if 143 + 100 > x > 143 and 0 + 4 > y >= 0:
                Map = path2
                x = 450
                y = 580
                path2bool = True
                path3bool = False
            if 780 + 20 >= x >= 780 and 259 + 40>= y >= 259:
                Map = sunkenChapel
                x = 15 
                y = 106
                sunkenChapelbool = True
                path3bool = False
            if 70 + 35 >= x >= 70 and 259 + 20>= y >= 259 and click[0] == 1:
                Map = house2
                x = 700
                y = 416
                path3bool = False
                house2bool = True

        if house2bool:
            if 712 + 70 >= x >= 712 and 407 + 70 > y >= 407 and click[0] == 1:
                Map = path3
                x = 90
                y = 300
                path3bool = True
                house2bool = False

        if sunkenChapelbool:
            if 0 + 12 >= x >= 0 and 90 + 60>= y >= 90:
                Map = path3
                x = 760
                y = 290
                path3bool = True
                sunkenChapelbool = False
            
                

            

        player2 = pygame.transform.flip(chara, 1, 0)




       # print("PATH BOOL = " + str(path2bool), "X = " , x , " Y = " , y)




        mouse = pygame.mouse.get_pos()
        gameDisplay.blit(Map, (0,0))

        healthBar(health)
        #print(mouse)

        #character(player2, 100,500)
        #character(player, x,y)
        if x_pos < 0:
            rotate = False
        elif x_pos > 0:
            rotate = True

        if not rotate:
            character(player2, x,y, attack)
        else:
            character(chara, x,y, attack)

        attack = False;

        #def button(x, y, w, h, px, py, action=None, *args)
        #def world(Map, chara ,mx, my, px, py):
        #def game_loop(Map, chara, mx, my, px, py):


        #print(enter)


        #if enter and homeTownbool:
            #print(enter)
         #   button(50, 300, 50, 50, x, y, game_loop, homeTown, player, 0, 0, 155, 340, health)
        #elif enter:
            #print(enter, "outside")
         #   button(155, 340, 25, 30, x, y, game_loop, house1, player_h1, 0, 0, 50, 300, health)
         #   button(545, 340, 25, 30, x, y, game_loop, house1, player_h1, 0, 0, 50, 300, health)



        testD = {'plyr': (x,y), 'bounds': [(0,0), (display_width,0), (0, display_height),(display_width,display_height)]}
        #print(testD['bounds'])
        list1 = testD['bounds']
        p1, p2, p3, p4 = list1
        o1, o2 = p1
##        p1 = list1[0]
##        p2 = list1[1]
##        p3 = list1[2]
        #print(p1, p2, p3, p4, "-----------", o1, o2)


        pygame.display.update()
        clock.tick(15)


#game_intro() 

game_loop(homeTown, player, 0, 0, 380, 555, 100)
#pygame.quit()
#quit()
