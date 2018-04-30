import pygame


display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
blue = (0, 0, 255)
homeTown = pygame.image.load('hometown.png')
lavaLake = pygame.image.load('Lava_Lake_MapAM.png')
pygame.init()
pygame.display.set_caption('Boyo RPG: A New Day')
clock = pygame.time.Clock()





def gameLoop():
  gameDisplay.blit(homeTown, (0,0))
  X2 = [40, 50, 60, 500]
  Y2 = [400, 500, 600, 300] 
  W2 = [5, 10, 15, 200]
  H2 = [20, 25, 30, 400]
  ColList = [None] * len(X2)
  n = 0
  for x in range(3):
    for x1, y1, w1, h1 in zip(X2, Y2, W2, H2):
       print("xar = ", x1, "yarg = ", y1, "w = ", w1," h= ", h1)
       pygame.draw.rect(gameDisplay, blue, (x1, y1, w1, h1))
       if n > len(ColList)-1:
         n = 0
       ColList[n] = [x1, y1, w1, h1]
       n+=1
       print("and now we check if the player collides with any of these") 
       print(ColList)





    boolDict = {"homeTown": True, "house1": False, "house2":False}
    HT = boolDict["homeTown"] #possible example
    if HT:
      boolDict["homeTown"] = False
      boolDict["house1"] = True
      print("ZERO")
    if boolDict["house1"]:
      boolDict["house1"] = False
      boolDict["house2"] = True
      print("ONE")
    if boolDict["house2"]:
      boolDict["house2"] = False
      boolDict["homeTown"] = True
      print("TWO")

    print("======== BOOL LIST")
    boolList = [True, False, False]
    if boolList[0]:
      boolList[0] = not boolList[0]
      boolList[2] = not boolList[2]
      print("ZERO")
    if boolList[1]:
      boolList[1] = not boolList[1]
      boolList[2] = not boolList[2]
      print("ONE")
    if boolList[2]:
      boolList[0] = not boolList[0]
      boolList[1] = not boolList[1]
      print("TWO")
      
    pygame.display.update()
    clock.tick(15)
    

gameLoop()
