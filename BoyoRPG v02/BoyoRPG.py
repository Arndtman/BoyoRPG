import pygame
import time
import random
from tkinter import *
from imp import reload
import PlayerTest; reload(PlayerTest)


#################################################
#Welcome to BoYo RpG Beta Source
#Acarndt@ucsc.edu 
#This game uses pygame to handle all the graphics
#So far generation is playerTest.py
#BoyoRPG.py is responsible for UI/Logic atm. 
#
#
###To Do####
#World Interaction. 
#Implement mobs. 
#Combat.
#Bounds checking.
#
#################################################

#main menu song is edited version of
#https://www.youtube.com/watch?v=4q-M8B9mGgs

##############CHANGELOG############
####4/16##
#Axel added better axis movement in gameloop
#Alex added gameloop() args, modified intro(), and button_mm for that
#Alex updated player PNG and added swing animation

####4/22##
##NOTE: (broken during integration) is Alex's fault atm will be updated
#
#Alex linked maps, added hp bar, and integrated the following into v02:
#Axel added rough boundary checking (broken during integration)
#Diego added inventory (broken during integration)
#Jack added loading screen



App = Tk()
App.title('BoYoRPG v021');

Message (App, text = "\t\BoYoRPG v021\n"

         "\n"

         "Welcome: to BoYoRPG v021 4/22 \n"
         "NOTE: House1 has full bounds (shown with test rects)!\n"
         "Movement: WASD \n"
         "Attacks: Left Mouse \n"
         "Mute/Unmute theme music: K/J\n"
         "Menu: p\n"
         "Enter Houses: Left Mouse \n \n"
         "Every Path and House will take you somewhere!\n"
         "(except for homeTown castle) :( \n"
         "\n"
         "Basic Inventory implemented (buggy to due integration)\n"
         "Rough Boundaries added (buggy to due integration) \n"
         "Maps linked via hardcode \n"
         "Added health bar and loading screen (% based) \n"
         "yes I know the swing sound is very buggy\n\n"
         "I may have missed something to implement, and also \n"
         "Report any bugs as there are some movement/animation ones. \n"
         "Try to exit the game and recreate them first\n\n"
         "Hit that RED [X] on top right to start the game! \n",
         fg = "blue", bg = "powder blue", bd = 20,
         relief = GROOVE, font=('arial', 20, 'bold')).pack(padx=10, pady=10)
App.mainloop()

pygame.init()
pygame.display.set_caption('Boyo RPG: A New Day')
clock = pygame.time.Clock()

pygame.mixer.music.load("MM.wav")

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

yellow = (255, 255, 0)
purple = (128, 0, 128)
grey = (128, 128, 128)
teal = (0, 128, 128)

#offset colors for menu flare
bgreen = (25, 209, 47) 
bred = (255, 114, 92)
bblue = (0, 0, 139)

lteal = (0, 158, 158)
magenta = (255, 0, 255)
silver = (192, 192, 192)


pause = False

enter = False

attack = False

rotate = True

#Maps
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

#Player
player = pygame.image.load('knight1.png')
playerAtk = pygame.image.load('knight2.png')
att = pygame.image.load('att.png')

#Main Menu + Pause Menu
MMInto = pygame.image.load('MM.png')
menu = pygame.image.load('Inventory.png')

#Map Booleans
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

def loadScreen():
    done = False
    expand = 0
    loadclock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT+1,2000)

    while done ==False:
     
        gameDisplay.fill(white)
        gameDisplay.blit(MMInto, (0,0))
        pygame.draw.rect(gameDisplay, green, (200,525,expand,50))
        pygame.display.update()
        loadclock.tick(60)
        if expand < 500:
            #expand += 20
            expand += random.randint(0, 35)
    
        if pygame.event.get(pygame.USEREVENT+1):
            done = True

#returns a manipulatable COLOR-ed rectangle
#with TEXT written on it.
#used for button creation
#Very generic
def text_objects(text, font, color=None):
    if color == None:
        color = black
    textSurface = font.render(text, True, color) #true is anti-alaisng
    return textSurface, textSurface.get_rect() 

#designates rectangular area of screen as interactable
#c1 = color, c2 = highlighted mouseover effect color
def button_mm(msg, x, y, w, h, c1, c2, action=None, arg1=None, arg2=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() 
    #print(mouse)
    #print(click) 
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, c2, (x, y, w, h))
        if click[0] == 1 and action != None :
            if arg1 == None and arg2 == None: 
               action() #runs object as function
            elif arg1 != None and arg2 == None: 
               action(arg1) #runs object as function
            else:
                action(arg1, arg2) 
    else:
        pygame.draw.rect(gameDisplay, c1, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)



def unpause():
    global pause
    pygame.mixer.music.unpause() 
    pause = False

def paused(pInst, wInst):

    pygame.mixer.music.pause() 
    
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    #print("IN PAAAUSSEDD") 
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white) 
        
        button_mm("Continue",280, 350, 100, 50, green, bgreen, unpause)
        #pass game_loop object 
        button_mm("Quit", 400, 350, 100, 50, red, bred, quitGame)
        #print("IN PAUSE BOOL") 
        button_mm("Inventory", 340, 420, 100, 50, blue, bblue, inventory, pInst, wInst)
        #print("LAEVIGN PAUSE") 
        #mouse = pygame.mouse.get_pos()
        #print(mouse)
 
        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True
    x = 380
    y = 555
    #These are to demonstrate zip function in playWorld  Class
    Xrect = [40, 50, 60]
    Yrect = [400, 500, 600]
    xWidth = [5, 10, 15]
    yHeight = [20, 25, 30]
    ##
    pygame.mixer.music.play(-1) #-1 loop, 1= play 1 + 1, so 5=6plays
    playIntro = PlayerTest.World(0,0, MMInto)
    playChar = PlayerTest.Player(x,y, player)
    playWorld = PlayerTest.World(0,0, homeTown)
    playWorld.mapLinks(Xrect, Yrect, xWidth, yHeight)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        playIntro.displayWorld()        
        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("BoYo RpG", largeText, gold)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


        button_mm("Play Beta",290, 350, 100, 50, green, bgreen, game_loop,
                  playChar, playWorld)
        #pass game_loop object 
        button_mm("Quit Beta", 390, 350, 110, 50, red, bred, quitGame) 
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        
        pygame.display.update()
        clock.tick(15)

# display and modify inventory
# note: for most buttons here, unpause is just a place holder
# need to implement functions later
def inventory(pInst, wInst):
    #print("IN INV")
    invent = PlayerTest.World(0, 0, menu)
    invent.displayWorld()
    #wInst.Map = menu
    #wInst.displayWorld()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos();

        # display character health as a health bar
        pygame.draw.rect(gameDisplay, black, (130, 25, 110, 40))
        pygame.draw.rect(gameDisplay, red, (135, 30, pInst.health, 30))

        # navigation buttons
        button_mm("Back", 300, 500, 100, 50, gold, yellow, game_loop,
                  pInst, wInst)
        button_mm("Save", 200, 500, 100, 50, green, bgreen, unpause)
        button_mm("Exit", 100, 500, 100, 50, red, bred, quitGame)

        # each inventory slot is a button
        for i in range(20):
            if (i%20 <10):
                button_mm("", 30+(i*70), 110, 70, 75, teal, lteal, selected)
            else:
                button_mm("", 30+((i-10)*70), 185, 70, 75, teal, lteal, selected)
            # fix math to make buttons look better

        # inventory slots for the active armor/weapon
        
        # if the mouse has selected an item, show these buttons
        if pause == True:
            button_mm("Drop", 400, 500, 100, 50, purple, magenta, unpause)
            button_mm("Add", 500, 500, 100, 50, grey, silver, unpause)
            button_mm("Swap", 600, 500, 100, 50, grey, silver, unpause)

        pygame.display.update()
        clock.tick(15)

def selected():
    #pygame.draw.lines(gameDisplay, yellow, True, ())
    unpause()

def deleteFromInv():
    unpause()

def function():
    pass


def game_loop(playChar, playWorld):
    global pause
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
    #AM 4/16/18: added x_posA/B and y_posA/B to fix movement
    x_pos = 0
    x_posA = 0
    x_posB = 0
    y_pos = 0
    y_posA = 0
    y_posB = 0
    gameExit = False
    attack = False
    while not gameExit:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #exit key
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_posA = -5
                if event.key == pygame.K_d:
                    x_posB = 5
                if event.key == pygame.K_w:
                    y_posA = -5
                if event.key == pygame.K_s:
                    y_posB = 5
                if event.key == pygame.K_k:
                    pygame.mixer.music.pause()
                if event.key == pygame.K_j:
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_p:
                    pause = True
                    paused(playChar, playWorld)
                if event.key == pygame.K_j:
                    mouse = pygame.mouse.get_pos()
                    print("===========================")
                    print("Mouse = ", mouse)
                    print("Char Tpright corner = (",playChar.x,",",playChar.y, ")")
            
            #AM 4/16/18: rewrote unpressed button event 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_posA = 0
                if event.key == pygame.K_d:
                    x_posB = 0
                if event.key == pygame.K_w:
                    y_posA = 0
                if event.key == pygame.K_s:
                    y_posB = 0
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            attack = True
            swing.play()
            playChar.health -= 1

        currentmap = playWorld.Map
        
        
        #AM 4/16/18: rewrote future position calculation
        x_pos = x_posA + x_posB
        y_pos = y_posA + y_posB
      
        #print("at =" playChar.x+x_pos, playChar.y+y_pos)
        #print("Collision at (", playChar.x, " ,", playChar.y, ") going ", x_pos, ", ", y_pos)
        footRect = pygame.Rect(playChar.x+x_pos, 33 + playChar.y+y_pos, 30, 2)
        if homeTownbool:
            house1Rect = pygame.Rect(105, 250, 115, 125)
            house2Rect = pygame.Rect(515, 250, 115, 125) 
            if footRect.colliderect(house1Rect) or footRect.colliderect(house2Rect):
                print("Collision at (", playChar.x, " ,", playChar.y, ") going ", x_pos, ", ", y_pos)
            #x_pos -= x_pos          
            #y_pos -= y_pos
                if playChar.x != 0:
                    x_pos = 0
                if playChar.y != 0:
                    y_pos = 0
            if 340 + 100 >= playChar.x >= 340 and 588 + 12 >= playChar.y >= 588:
                playWorld.Map = path2
                playChar.x = 555
                playChar.y = 25
                path2bool = True
                homeTownbool = False
            if 140 + 30 >= playChar.x >= 140 and 340 + 15 > playChar.y >= 340 and click[0] == 1:
                playWorld.Map = house1
                playChar.x = 245
                playChar.y = 465
                homeTownbool = False                
                house1bool = True  
            if 550 + 30 >= playChar.x >= 550 and 335 + 15 > playChar.y >= 335 and click[0] == 1:
                house1Flip = pygame.transform.flip(house1, 1, 0)
                playWorld.Map = house1Flip
                playChar.x = 525
                playChar.y = 470
                homeTownbool = False
                house1Flipbool = True
            
        w1 = w2 = w3 = w4 = w5 = w6 = w7 = w8= w9 = w10 = w11 = None
        
        testList = []
        if house1bool:
            if 225 + 60 >= playChar.x >= 225 and 402 + 15 > playChar.y >= 402 and click[0] == 1:
              playWorld.Map = homeTown
              playChar.x = 190
              playChar.y = 360
              house1bool = False
              homeTownbool = True
              del testList[:] #clear for next run
              
            w1 = pygame.Rect(0, 0, 40, 800)
            w2 = pygame.Rect(40, 570, 760, 15)
            w3 = pygame.Rect(40, 240, 465, 190)
            w4 = pygame.Rect(120, 440, 80, 100)
            w5 = pygame.Rect(620, 350, 150, 165)
            w6 = pygame.Rect(235, 100, 80, 110)
            w7 = pygame.Rect(40, 40, 760, 60)
            w8 = pygame.Rect(625, 120, 150, 145)
            w9 = pygame.Rect(315, 70, 75, 60)
            w10 = pygame.Rect(505, 80, 620, 45)
            w11 = pygame.Rect(780, 90, 20, 510)

            testList.extend((w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11))
            
         #The following two are equivelent
            if footRect.collidelist(testList) != -1:
##            if footRect.colliderect(w1) or footRect.colliderect(w2) or footRect.colliderect(w3) \
##               or footRect.colliderect(w4) or footRect.colliderect(w5) or footRect.colliderect(w6) \
##               or footRect.colliderect(w7) or footRect.colliderect(w8) or footRect.colliderect(w9) \
##               or footRect.colliderect(w10) or footRect.colliderect(w11):
                print("Collision at (", playChar.x, " ,", playChar.y, ") going ", x_pos, ", ", y_pos)
            #x_pos -= x_pos          
            #y_pos -= y_pos
                if playChar.x != 0:
                    x_pos = 0
                if playChar.y != 0:
                    y_pos = 0
              

        if house1Flipbool:
            if 510 + 50 >= playChar.x >= 510 and 402 + 15 > playChar.y >= 402 and click[0] == 1:
              playWorld.Map = homeTown
              playChar.x = 535
              playChar.y = 345
              house1Flipbool = False
              homeTownbool = True

        if path2bool:
            if 533 + 60 > playChar.x > 510 and 0 + 3 > playChar.y >= 0:
                playWorld.Map = homeTown
                playChar.x = 380
                playChar.y = 555
                path2bool = False
                homeTownbool = True
            if 0 + 12 > playChar.x >= 0 and 380 + 100 > playChar.y > 380:
                playWorld.Map = bridge3
                playChar.x = 780
                playChar.y = 280
                path2bool = False
                bridgebool = True
            if 420 + 80 > playChar.x > 420 and 588 + 12 >= playChar.y >= 588:
                playWorld.Map = path3
                playChar.x = 170
                playChar.y = 15
                path2bool = False
                path3bool = True
            if 235 > playChar.x > 0 and 220 > playChar.y > 0:
                playChar.x -= 5
                playChar.y -= 5
            if 520 + 230 > playChar.x > 520 and 50 + 220 > playChar.y > 50:
                playChar.x -= 5
                playChar.y -= 5

        if bridgebool:
            if 780 + 20 > playChar.x > 780 and 240 + 60 > playChar.y > 240:
                playWorld.Map = path2
                playChar.x = 15
                playChar.y = 430
                path2bool = True
                bridgebool = False
            if 0 + 15 > playChar.x >= 0 and 290 + 80 > playChar.y > 290:
                playWorld.Map = forest1
                playChar.x = 770
                playChar.y = 270
                bridgebool = False
                forestbool = True
            if 700 + 80 >= playChar.x >= 700 and 0 + 10>= playChar.y >= 0:
                playWorld.Map = cliff
                playChar.x = 625
                playChar.y = 530
                cliffbool = True
                bridgebool = False
                
        if cliffbool:
            if 500 + 260 >= playChar.x >= 500 and 580 + 20>= playChar.y >= 580:
                playWorld.Map = bridge3
                playChar.x = 740
                playChar.y = 15
                cliffbool = False
                bridgebool = True
            if 640 + 35 >= playChar.x >= 635 and 70 + 20>= playChar.y >= 70:
                playWorld.Map = lavaLake
                playChar.x = 765
                playChar.y = 480
                lavaLakebool = True
                cliffbool = False

        if lavaLakebool:
            if 780 + 20 >= playChar.x >= 780 and 430 + 80>= playChar.y >= 430:
                playWorld.Map = cliff
                playChar.x = 655
                playChar.y = 110
                lavaLakebool = False
                cliffbool = True
        
                
        if forestbool:
            if 780 + 20 > playChar.x > 780 and 255 + 50 > playChar.y > 255:
                playWorld.Map = bridge3
                playChar.x = 15
                playChar.y = 315
                bridgebool = True
                forestbool = False

        if path3bool:
            if 143 + 100 > playChar.x > 143 and 0 + 4 > playChar.y >= 0:
                playWorld.Map = path2
                playChar.x = 450
                playChar.y = 580
                path2bool = True
                path3bool = False
            if 780 + 20 >= playChar.x >= 780 and 259 + 40>= playChar.y >= 259:
                playWorld.Map = sunkenChapel
                playChar.x = 15 
                playChar.y = 105
                sunkenChapelbool = True
                path3bool = False
            if 70 + 35 >= playChar.x >= 70 and 259 + 20>= playChar.y >= 259 and click[0] == 1:
                playWorld.Map = house2
                playChar.x = 700
                playChar.y = 415
                path3bool = False
                house2bool = True

        if house2bool:
            if 712 + 70 >= playChar.x >= 712 and 407 + 70 > playChar.y >= 407 and click[0] == 1:
                playWorld.Map = path3
                playChar.x = 90
                playChar.y = 300
                path3bool = True
                house2bool = False

        if sunkenChapelbool:
            if 0 + 12 >= playChar.x >= 0 and 90 + 60>= playChar.y >= 90:
                playWorld.Map = path3
                playChar.x = 760
                playChar.y = 290
                path3bool = True
                sunkenChapelbool = False

        
        if random.randint(0, 100) < 12:
            if playWorld.Map != currentmap:
                loadScreen()
        
        playChar.move(x_pos,y_pos)
   
        playWorld.displayWorld()
        pygame.draw.rect(gameDisplay, gold, footRect, 2)
        pygame.draw.rect(gameDisplay, red, (playChar.x, playChar.y, 30, 35), 1)
        attack = playChar.displayCharacter(x_pos, attack)
        playChar.healthBar()

        if w1 != None: 
            pygame.draw.rect(gameDisplay, blue, w1)
            pygame.draw.rect(gameDisplay, blue, w2)
            pygame.draw.rect(gameDisplay, blue, w3)
            pygame.draw.rect(gameDisplay, blue, w4)
            pygame.draw.rect(gameDisplay, blue, w5)
            pygame.draw.rect(gameDisplay, blue, w6)
            pygame.draw.rect(gameDisplay, blue, w7)
            pygame.draw.rect(gameDisplay, blue, w8)
            pygame.draw.rect(gameDisplay, blue, w9)
            pygame.draw.rect(gameDisplay, blue, w10)
            pygame.draw.rect(gameDisplay, blue, w11)

       

        pygame.display.update()
        clock.tick(15)
        


game_intro() 
#pygame.quit() 
#quit()    
