import pygame
import time
import random

#from PlayerTest import * 
 

pygame.init()
pygame.display.set_caption('Boyo RPG')
clock = pygame.time.Clock()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255) 

pause = False

enter = False

homeTown = pygame.image.load('hometown.png')
player = pygame.image.load('player.png')
house = pygame.image.load('house1.png')
player_h1 = pygame.image.load('player_h1.png') 



gameDisplay = pygame.display.set_mode((display_width, display_height))


def quitGame():
    pygame.quit()
    quit()

def character(chara, x,y):
    gameDisplay.blit(chara, (x,y))



#button(155, 340, 25, 30, x, y, game_loop, house, player_h1, 0, 0, 50, 300)

def button(x, y, w, h, px, py, action=None, *args): #action=None
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global enter
    
    if x + w > px > x and y + h > py > y:
        print('almost (click to enter)') 
        if click[0] == 1 and action != None:
            print('yea')
            enter = not enter
            action(*args) #runs object as function
    else:
        print('no')

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


def game_intro():
    intro = True
    #pygame.mixer.music.play(-1) #-1 loop, 1= play 1 + 1, 5=6plays
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("BoYo RpG", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Play Beta",250, 350, 100, 50, green, bgreen, game_loop)
        #pass game_loop object 
        button("Quit, Like Beta", 350, 350, 100, 50, red, bred, quitGame) 
        mouse = pygame.mouse.get_pos()
        #print(mouse)
 
        pygame.display.update()
        clock.tick(15) 
        
        

def game_loop(Map, chara, mx, my, px, py):
    global pause
    global enter 
    rotate = True 
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
                if event.key == pygame.K_LEFT: #left arrow
                    x_pos = -5
                if event.key == pygame.K_RIGHT:
                    x_pos = 5
                if event.key == pygame.K_UP: #left arrow
                    y_pos = -5
                if event.key == pygame.K_DOWN:
                    y_pos = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_pos = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  
                    y_pos = 0
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
    
        player2 = pygame.transform.flip(chara, 1, 0)
         
        mouse = pygame.mouse.get_pos()
        gameDisplay.blit(Map, (0,0))


        print(mouse)

        #character(player2, 100,500)
        #character(player, x,y) 
        if x_pos < 0: 
            rotate = False
        elif x_pos > 0:
            rotate = True

        if not rotate:
            character(player2, x,y)
        else:
            character(chara, x,y)

        #def button(x, y, w, h, px, py, action=None, *args)
        #def world(Map, chara ,mx, my, px, py):
        #def game_loop(Map, chara, mx, my, px, py):


        #print(enter) 

        
        if enter:
            #print(enter)
            button(50, 300, 50, 50, x, y, game_loop, homeTown, player, 0, 0, 155, 340)       
        else:
            #print(enter, "outside") 
            button(155, 340, 25, 30, x, y, game_loop, house, player_h1, 0, 0, 50, 300)
            button(545, 340, 25, 30, x, y, game_loop, house, player_h1, 0, 0, 50, 300)
            
        
        
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
        

game_loop(homeTown, player, 0, 0, 380, 555) 
#pygame.quit() 
#quit()    
