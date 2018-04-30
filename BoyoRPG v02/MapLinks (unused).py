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
            
