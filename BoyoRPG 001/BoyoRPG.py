import pygame
import time
import random
from imp import reload
import PlayerTest; reload(PlayerTest)


#################################################
#Welcome to BoYo RpG Source
#This game uses pygame to handle all the graphics
#So far generation is playerTest.py
#BoyoRPG.py is responsible for UI/Logic atm. 
#
#
###To Do####
#World Interaction. 
#Implement mobs. 
#Combat.
#
#################################################

#main menu song is edited version of
#https://www.youtube.com/watch?v=4q-M8B9mGgs 

pygame.init()
pygame.display.set_caption('Boyo RPG: A New Day')
clock = pygame.time.Clock()

pygame.mixer.music.load("MM.wav")

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


homeTown = pygame.image.load('hometown.png')
player = pygame.image.load('player.png')
house = pygame.image.load('house1.png')
player_h1 = pygame.image.load('player_h1.png')
MMInto = pygame.image.load('MM.png')


gameDisplay = pygame.display.set_mode((display_width, display_height))

def quitGame():
    pygame.quit()
    quit()

#returns a manipulatable COLORed rectangle
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



def unpause():
    global pause
    pygame.mixer.music.unpause() 
    pause = False

def paused():

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
        #gameDisplay.fill(white) 
        
        button_mm("Continue",280, 350, 100, 50, green, bgreen, unpause)
        #pass game_loop object 
        button_mm("Quit", 400, 350, 100, 50, red, bred, quitGame)
        button_mm("Inventory", 340, 420, 100, 50, blue, bblue, unpause)
        mouse = pygame.mouse.get_pos()
        #print(mouse)
 
        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    pygame.mixer.music.play(-1) #-1 loop, 1= play 1 + 1, 5=6plays
    playIntro = PlayerTest.World(0,0, MMInto)
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


        button_mm("Play Beta",250, 350, 100, 50, green, bgreen, game_loop)
        #pass game_loop object 
        button_mm("Quit, Beta", 350, 350, 200, 50, red, bred, quitGame) 
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        
        pygame.display.update()
        clock.tick(15) 

def game_loop():
    global pause
    x = 380
    y = 555
    x_pos = 0
    y_pos = 0
    gameExit = False
    playChar = PlayerTest.Player(x,y, player)
    playWorld = PlayerTest.World(0,0, homeTown) 
    while not gameExit:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #exit key
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_pos = -5
                if event.key == pygame.K_d:
                    x_pos = 5
                if event.key == pygame.K_w:
                    y_pos = -5
                if event.key == pygame.K_s:
                    y_pos = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_j:
                    mouse = pygame.mouse.get_pos()
                    print("===========================")
                    print("Mouse = ", mouse)
                    print("Tpright corner = (",playChar.x,",",playChar.y, ")")
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_pos = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_pos = 0
        
        mouse = pygame.mouse.get_pos()
        
        playChar.move(x_pos,y_pos)

    
        playWorld.displayWorld() 
        playChar.displayCharacter(x_pos)

        pygame.display.update()
        clock.tick(15)
        


game_intro() 
#pygame.quit() 
#quit()    
