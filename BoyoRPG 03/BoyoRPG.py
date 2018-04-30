import pygame
import time
import random
from tkinter import *
from imp import reload
import PlayerTest; reload(PlayerTest)
import MapLinks; reload(MapLinks)


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

###4/29##
#Axel updated boundary checking, yet to be fully implemented for all maps
#Alex integrated 4/22 to 4/29 into BoyoRPG v03, debugged attacks,
##load screens, fulfilled deathscreen, and added main menu label.png.
##Also restructured code to run from main() as opposed to game_intro()
##(This is to restart the game)
#Jack wrote loadscreen() some deathscreen, and implemented character movement
##(still need Yaxis)
#Diego wrote inventory (unfinished)

App = Tk()
App["bg"] = "black"
photo = PhotoImage(file = "png/label.png")
label = Label(App, image=photo)
label.pack()

App.title('BoYoRPG v03');

Message (App, text = "\t\BoYoRPG v03\n"

         "\n"
         "Welcome: to BoYoRPG v03 4/29 \n"
         "Movement: WASD \n"
         "Attacks: Left Mouse \n"
         "Mute/Unmute theme music: K/J\n"
         "Menu: P\n"
         "Enter Houses: Left Mouse \n \n"
         "Every Path and House will take you somewhere!\n"
         "(except for homeTown castle) :( \n"
         "\n"
         "Changelog:\n"
         "Basic Inventory implemented (buggy to due integration)\n"
         "Bounds fulfilled \n"
         "Fixed Attack bugs, added movement animation (still need Yaxis)\n"
         "Also added deathscreens and corrected restart on death\n"
         "\n"
         "I may have missed something to implement, and also \n"
         "Report any bugs as there are some movement/animation ones. \n"
         "Try to exit the game and recreate them first\n\n"
         "Close this window to start the game! \n",
         fg = "ivory", bg = "dark slate blue", bd = 20,
         relief = GROOVE, font=('arial', 20, 'bold')).pack(padx=10, pady=10)
App.mainloop()

pygame.init()
pygame.display.set_caption('Boyo RPG: A New Day')
clock = pygame.time.Clock()

homeTown = pygame.image.load('png/hometown.png')

pygame.mixer.music.load("wav/MM.wav")

swing = pygame.mixer.Sound('wav/swing.wav')
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

#Maps in MapLinks.py as of v21Clean

#Player
player = pygame.image.load('png/knight1.png')
playerLstride = pygame.image.load('png/strideleft.png')
playerLstride2 = pygame.image.load('png/playerLstride2.png')
playerRstride = pygame.image.load('png/strideright.png')
playerRstride2 = pygame.image.load('png/playerRstride2.png')
playerAtk = pygame.image.load('png/knight2.png')
att = pygame.image.load('png/att.png')

#Enemy
orc = pygame.image.load('png/orc.png')


#Main Menu + Pause Menu
MMInto = pygame.image.load('png/MM.png')
menu = pygame.image.load('png/Inventory.png')
dthScreen = pygame.image.load('png/deathscreen.png')
label = pygame.image.load('png/label.png')


gameDisplay = pygame.display.set_mode((display_width, display_height))

def quitGame():
    pygame.quit()
    quit()

def main():
    MapLinks.clear()
    game_intro()
    
#JE: 4/27 LoadScreen event
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
            expand += random.randint(0, 35)
    
        if pygame.event.get(pygame.USEREVENT+1):
            done = True
            
#AA: 4/29 Fulfilled deathscreen           
def cont(pInst, wInst):
    print("yep")
    pInst.health = 100
    playIntro = PlayerTest.World(0,0, dthScreen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        playIntro.displayWorld()        
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("BoYo RpG", largeText, gold)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


        button_mm("Play Again?",275, 350, 115, 50, green, bgreen, main)

##        button_mm("Play Again?",275, 350, 115, 50, green, bgreen, game_loop,
##                  pInst, wInst)
        #pass game_loop object 
        button_mm("Quit Beta", 390, 350, 110, 50, red, bred, quitGame) 
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15)

#JE: 4/29 DeathScreen similar to loadscreen
def deathScreen(pInst, wInst):
    
    done = False
    deathclock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT+1,2000)
    expand = 0
    while done ==False:
        gameDisplay.fill(white)
        gameDisplay.blit(dthScreen, (0,0))
        pygame.draw.rect(gameDisplay, green, (200,525,expand,50))
        pygame.display.update()
        deathclock.tick(60)
        if expand < 500:
            expand += random.randint(15, 35)
    
        if pygame.event.get(pygame.USEREVENT+1):
            done = True
    cont(pInst, wInst)


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
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button_mm("Continue",280, 350, 100, 50, green, bgreen, unpause)
        #pass game_loop object 
        button_mm("Quit", 400, 350, 100, 50, red, bred, quitGame)
        button_mm("Inventory", 340, 420, 100, 50, blue, bblue, inventory, pInst, wInst)
 
        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True
    x = 380
    y = 555
    pygame.mixer.music.play(-1) #-1 loop, 1= play 1 + 1, so 5=6plays
    playIntro = PlayerTest.World(0,0, MMInto)
    playChar = PlayerTest.Player(x,y, player)
    playWorld = PlayerTest.World(0,0, homeTown)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        playIntro.displayWorld()
        gameDisplay.blit(label, (340,430))
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
    #AM 4/16/18: added x_posA/B and y_posA/B to fix movement
    #AM 4/28/18: changed x/y_pos into x/y_vel(ocity) and moved them into Player object
    x_vel_A = 0
    x_vel_B = 0
    y_vel_A = 0
    y_vel_B = 0
    attack = False
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #exit key
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_vel_A = -5
                if event.key == pygame.K_d:
                    x_vel_B = 5
                if event.key == pygame.K_w:
                    y_vel_A = -5
                if event.key == pygame.K_s:
                    y_vel_B = 5
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
                    x_vel_A = 0
                if event.key == pygame.K_d:
                    x_vel_B = 0
                if event.key == pygame.K_w:
                    y_vel_A = 0
                if event.key == pygame.K_s:
                    y_vel_B = 0
            ##AA 4/27: fixed infinite attack bug        
            click = pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN and click[0] == 1:
                attack = True
                swing.play()
                playChar.health -= 16
        
        mouse = pygame.mouse.get_pos()
        
        #AM 4/16/18: rewrote future position calculation
        playChar.x_vel = x_vel_A + x_vel_B
        playChar.y_vel = y_vel_A + y_vel_B
      
        playWorld.displayWorld()
        #futurePlayRect = pygame.Rect(playChar.x + playChar.x_vel/2, playChar.y + playChar.y_vel/2, 30, 35)
       
       
        MapLinks.links(playChar, playWorld) 
        
        playChar.move()
        
        #pygame.draw.rect(gameDisplay, black, futurePlayRect, 1) 
        pygame.draw.rect(gameDisplay, red, (playChar.x, playChar.y, 30, 35), 1)
        attack = playChar.displayCharacter(attack)
        playChar.healthBar()

        if playChar.getHealth() <= 0:
            deathScreen(playChar, playWorld);

           

        pygame.display.update()
        clock.tick(15)
        


main()
#pygame.quit() 
#quit()    
