'''
Kenneth Horsman (UCID: 30260797)

Create a program that draws a house similar to the one shown below using the SimpleGraphics module
available on the course website.
While you are free to take some artistic license while creating your image, you must include the sky and
ground, a cloud, the sun, and a house with a door, window and roof that are all different colors. Include
your name in the lower right corner of the image.

Helpful site: https://www.plus2net.com/python/tkinter-colors.php
'''

from SimpleGraphics import *

def main():
    ### DIMENSIONS ###

    HOUSE_X = 50
    HOUSE_Y = 300
    HOUSE_WIDTH = 350
    HOUSE_LENGTH = 235
    HOUSE_RIGHT = HOUSE_X + HOUSE_WIDTH
    ROOF_TOP = HOUSE_Y - 125
    ROOF_LEFT = HOUSE_X - 25
    ROOF_RIGHT = HOUSE_X + HOUSE_WIDTH + 100
    BALCONY_Y = HOUSE_Y + HOUSE_LENGTH
    BALCONY_WIDTH = HOUSE_WIDTH + 75
    BALCONY_LENGTH = 15
    POST_WIDTH = 15
    POST_LENGTH = HOUSE_LENGTH
    DOOR_X = HOUSE_X + 50
    DOOR_Y = HOUSE_Y + 50
    DOOR_WIDTH = 100
    DOOR_LENGTH = HOUSE_LENGTH - 50
    WINDOW_X = HOUSE_X + 195
    WINDOW_Y = HOUSE_Y + 70
    WINDOW_WIDTH = 120
    WINDOW_LENGTH = 80
    WINDOW_CENTER_X = WINDOW_X + (WINDOW_WIDTH // 2)
    WINDOW_CENTER_Y = WINDOW_Y + (WINDOW_LENGTH // 2)


    # SKY BACKGROUND
    setOutline(244,160,175)
    setFill(244,160,175)
    rect(0,0, 800, 100) ## top

    setOutline(246,155,170)
    setFill(246,155,170)
    rect(0,100, 800, 100)

    setOutline(248,150,165)
    setFill(248,150,165)
    rect(0,200, 800, 75)

    setOutline(250,145,160)
    setFill(250,145,160)
    rect(0,275, 800, 125) ## bottom


    # SUN
    setOutline(255,205,0)
    setFill(255,205,0)
    ellipse(595,295, 85, 85) ## outer edge

    setOutline(255,210,0)
    setFill(255,210, 0)
    ellipse(600,300, 75, 75) ## inner circle


    # CLOUDS
    setOutline("thistle3") # (205,181,205)
    setFill("thistle3")
    blob(725,125, 575,125, 650,135, 700,95) ## bottom of upper right
    blob(650,50, 700,100, 545,80, 750,75, 675,125, 575,90, 625,95) ## upper right
    blob(500,125, 425,120, 500,140, 350,130) ## middle
    blob(50,80, 250,100, 275,75, 400, 90) ## top left
    blob(20,210, 60,220, 70,230, 160,215) ## left of house

    setOutline(210,170,190)
    setFill(210,170,190)
    blob(550,210, 600,200, 700,220, 750,210, 775,210, 575,175, 800,180, 650,225) ## just above sun

    setOutline(215,160,195)
    setFill(215,160,195)
    blob(500,310, 550,320, 600,300, 650, 310, 700,300, 630,310, 555,315, 640,330) ## over sun


    # GRASS
    setOutline("dark olive green") # (85,107,47)
    setFill(85,105,45)
    rect(0,400, 800, 200) ## base layer

    setFill(80,100,40)
    ellipse(0,399, 100, 10) ## just left of house
    ellipse(300,398, 250, 22) ## just right of house
    ellipse(500,399, 225, 10) ## under sun
    ellipse(640,395, 300, 20) ## right edge

    setFill(75,95,35)
    polygon(0,580, # above bottom left
            HOUSE_X,HOUSE_Y+HOUSE_LENGTH+BALCONY_LENGTH, # top left
            HOUSE_X+BALCONY_WIDTH,HOUSE_Y+HOUSE_LENGTH+BALCONY_LENGTH, # top right
            HOUSE_X+BALCONY_WIDTH-35,600, # bottom right
            0,600) # bottom left
            ## house shadow

    setFill(85,105,45)
    polygon(HOUSE_X+HOUSE_WIDTH-10,HOUSE_Y+HOUSE_LENGTH+BALCONY_LENGTH+15,  # top left
        HOUSE_X+BALCONY_WIDTH-35,HOUSE_Y+HOUSE_LENGTH+BALCONY_LENGTH+15,  # top right
        HOUSE_X+BALCONY_WIDTH-65,600,  # bottom right
        HOUSE_X+HOUSE_WIDTH-55,600)  # bottom left
        ## gap in house shadow


    # POND
    setOutline("bisque3") # (205,183,158)
    setFill("bisque3")
    blob(900,400, 690,400, 675,450, 700,500, 675,600, 700,700) ## sand

    setFill(195,175,150)
    blob(900,400, 710,400, 695,450, 715,500, 710,600, 800,700) ## wet sand

    setOutline("light steel blue") # (176,196,222)
    setFill(172,192,218)
    blob(900,410, 725,400, 700,450, 725,500, 725,600, 900,700) ## base water

    setFill("light steel blue")
    blob(715,460, 720,410, 825,415, 900,550, 850,700, 800,700, 750,600, 760,500) ## highlight


    # BASE OF HOUSE
    setOutline("wheat4") # (139,126,102)
    setFill(140,125,100)
    rect(HOUSE_X,HOUSE_Y,  HOUSE_WIDTH, HOUSE_LENGTH) ## base from (50,300) to (400, 550)
    
    setOutline(125,115,90)
    setFill(125,115,90)
    rect(HOUSE_X+POST_WIDTH,HOUSE_Y+5, HOUSE_WIDTH-POST_WIDTH, 5) ## horizontal post shadow
    rect(DOOR_X+DOOR_WIDTH,DOOR_Y, 5, DOOR_LENGTH) ## vertical door shadow
    rect(DOOR_X,DOOR_Y-5, DOOR_WIDTH+5, 5) ## horizontal door shadow
    rect(WINDOW_X+WINDOW_WIDTH,WINDOW_Y, 5, WINDOW_LENGTH+2) ## vertical window shadow
    rect(WINDOW_X,WINDOW_Y-5, WINDOW_WIDTH+5, 5) ## horiztonal window shadow

    setOutline(150,135,110)
    setFill(150,135,110)
    rect(HOUSE_X+HOUSE_WIDTH,HOUSE_Y,  5, HOUSE_LENGTH) ## right wall highlight

    # ROOF
    setOutline(80, 80, 80)
    setFill(70, 70, 70)
    polygon(ROOF_LEFT,HOUSE_Y,  ROOF_RIGHT,HOUSE_Y,  ROOF_RIGHT-150,ROOF_TOP,  ROOF_LEFT+125,ROOF_TOP)
    # polygon(bottom left corner, bottom right corner, top right corner, top left corner)

    setOutline(60,60,60)
    line_height = HOUSE_Y - 10 # I could/should have made more of these variables for other elements but I didn't feel like it
    line_start = ROOF_LEFT + 10
    line_end = ROOF_RIGHT - 10
    while line_height >= ROOF_TOP: 
        line(line_start,line_height, line_end,line_height) ## lines across roof
        line_start += 15
        line_end -= 18
        line_height -= 15

    setOutline(105,105,100)
    setFill(105,105,100)
    polygon(500,300, 505,300, 355,175, 350,175) ## roof highlight


    # DOOR
    setOutline(35,35,35) # Black is (0,0,0)
    setFill(40, 40, 40)
    rect(DOOR_X,DOOR_Y, DOOR_WIDTH, DOOR_LENGTH) ## base from (100,350) to (200,535)

    setOutline(40,40,40)
    setFill(38,38,38)
    rect(DOOR_X+10,DOOR_Y+15, 35, 80) # upper left indent outline
    rect(DOOR_X+55,DOOR_Y+15, 35, 80) # upper right indent outilne
    rect(DOOR_X+10,DOOR_Y+100, 80, 75) # bottom indent outline

    setOutline(39,39,39)
    setFill(38,38,38)
    rect(DOOR_X+15,DOOR_Y+20, 25, 70) # upper left indent
    rect(DOOR_X+60,DOOR_Y+20, 25, 70) # upper right indent
    rect(DOOR_X+15,DOOR_Y+105, 70, 65) # bottom indent

    setOutline(100,60,20) # tan4 is (139,90,43)
    setFill(80, 55, 40)
    ellipse(DOOR_X+DOOR_WIDTH-15,DOOR_Y+90, 10, 10) ## knob


    # WINDOW
    setOutline(30, 30, 30)
    setFill(205, 200, 115) # khaki3 is (205,198,115)
    rect(WINDOW_X,WINDOW_Y, WINDOW_WIDTH, WINDOW_LENGTH) ## base from (245,370) to (365,450)

    setOutline(210, 205, 120)
    setFill(215, 210, 125)
    polygon(246,411, 246,448, 286,448, 363,409, 363,371, 324,371) # highlight
    # polygon(bottom upper, bottom corner, bottom right, top lower, top corner, top left)
    
    setOutline(30, 30, 30)
    line(WINDOW_X,WINDOW_CENTER_Y,  WINDOW_X+WINDOW_WIDTH,WINDOW_CENTER_Y) ## horizontal line
    line(WINDOW_CENTER_X,WINDOW_Y,  WINDOW_CENTER_X,WINDOW_Y+WINDOW_LENGTH) ## vertical line


    # MY KITTY!
    setOutline(50,50,50)
    setFill(50,50,50)
    pieSlice(WINDOW_CENTER_X+25,WINDOW_Y+WINDOW_LENGTH-8, 15, 14, 0, 180) ## head

    pieSlice(WINDOW_CENTER_X+19,WINDOW_Y+WINDOW_LENGTH-3, 5, 3, 0, 180) ## left paw
    pieSlice(WINDOW_CENTER_X+42,WINDOW_Y+WINDOW_LENGTH-3, 5, 3, 0, 180) ## right paw

    polygon(WINDOW_CENTER_X+26,WINDOW_Y+WINDOW_LENGTH-3, 
        WINDOW_CENTER_X+34,WINDOW_Y+WINDOW_LENGTH-6, 
        WINDOW_CENTER_X+25,WINDOW_Y+WINDOW_LENGTH-10) ## left ear
    
    polygon(WINDOW_CENTER_X+39,WINDOW_Y+WINDOW_LENGTH-3, 
            WINDOW_CENTER_X+31,WINDOW_Y+WINDOW_LENGTH-6, 
            WINDOW_CENTER_X+40,WINDOW_Y+WINDOW_LENGTH-10) ## right ear

    setOutline(140,140,140)
    line(WINDOW_CENTER_X+21,WINDOW_Y+WINDOW_LENGTH-2, WINDOW_CENTER_X+24,WINDOW_Y+WINDOW_LENGTH-2) ## left mitten
    line(WINDOW_CENTER_X+44,WINDOW_Y+WINDOW_LENGTH-2, WINDOW_CENTER_X+47,WINDOW_Y+WINDOW_LENGTH-2) ## right mitten

    blob(WINDOW_CENTER_X+31,WINDOW_Y+WINDOW_LENGTH-1,
        WINDOW_CENTER_X+31,WINDOW_Y+WINDOW_LENGTH-2,
        WINDOW_CENTER_X+32,WINDOW_Y+WINDOW_LENGTH-1,
        WINDOW_CENTER_X+33,WINDOW_Y+WINDOW_LENGTH,
        WINDOW_CENTER_X+34,WINDOW_Y+WINDOW_LENGTH-2,
        WINDOW_CENTER_X+32,WINDOW_Y+WINDOW_LENGTH-1) ## moustache

    setOutline(110,125,50) # subtle greenish color
    setFill(150,160,80) # yellower-highlight
    ellipse(WINDOW_CENTER_X+29,WINDOW_Y+WINDOW_LENGTH-5, 2, 2)  ## left eye
    ellipse(WINDOW_CENTER_X+35,WINDOW_Y+WINDOW_LENGTH-5, 2, 2)  ## right eye

    setOutline(30,30,30)
    rect(WINDOW_X, WINDOW_Y+WINDOW_LENGTH-1, WINDOW_WIDTH, 2)  ## thickened windowsill


    # BALCONY
    setOutline("azure4") # (131,139,139)
    setFill("azure4")
    rect(HOUSE_X,BALCONY_Y, BALCONY_WIDTH, BALCONY_LENGTH) ## base from (50,535) to (475,550)

    setFill(125,135,135)
    rect(HOUSE_X + POST_WIDTH,BALCONY_Y - 5, HOUSE_WIDTH, 5) ## top shadow

    setFill(135,145,145)
    rect(HOUSE_X+HOUSE_WIDTH-5,HOUSE_Y+HOUSE_LENGTH-5, 65, 5) ## gap highlight
    line(HOUSE_X+BALCONY_WIDTH-1,HOUSE_Y+HOUSE_LENGTH+1, HOUSE_X+BALCONY_WIDTH-1,HOUSE_Y+HOUSE_LENGTH+BALCONY_LENGTH) ## right highlight


    # POSTS
    setOutline("burlywood4") # (139,115,85)
    setFill(140,115,85)
    rect(HOUSE_X,HOUSE_Y+1, POST_WIDTH, POST_LENGTH) ## left post
    rect(HOUSE_X+BALCONY_WIDTH-POST_WIDTH,HOUSE_Y+1, POST_WIDTH, POST_LENGTH) ## right post
    rect(HOUSE_X,HOUSE_Y+1, BALCONY_WIDTH, 5) ## horizonal post

    setOutline(155,130,100)
    line(HOUSE_X+POST_WIDTH,HOUSE_Y+10, HOUSE_X+POST_WIDTH,HOUSE_Y+HOUSE_LENGTH) ## left post highlight
    line(HOUSE_X+BALCONY_WIDTH-1,HOUSE_Y+1, HOUSE_X+BALCONY_WIDTH-1,HOUSE_Y+HOUSE_LENGTH) ## right post highilght

    setOutline(125,100,70)
    setFill(125,100,70)
    rect(HOUSE_X,HOUSE_Y+1, BALCONY_WIDTH, 2) ## roof shadow


    # BENCH
    setOutline(110,85,55)
    setFill(110,85,55)
    rect(WINDOW_X+5,BALCONY_Y-35, 110, 10) ## bench seat
    rect(WINDOW_X+5,BALCONY_Y-25, 10, 22) ## left leg
    rect(WINDOW_X+105,BALCONY_Y-25, 10, 22) ## right leg

    setOutline(95,70,40)
    line(WINDOW_X+4,BALCONY_Y-35, WINDOW_X+4,BALCONY_Y-3) ## left leg shadow
    line(WINDOW_X+104,BALCONY_Y-25, WINDOW_X+104,BALCONY_Y-3) ## right leg shadow

    # NAME
    setOutline("black")
    setFont("montserrat","8.5") # my favorite font!
    text(5, 590, "Made by Kenneth Horsman", "w")

if __name__=="__main__":
    main()