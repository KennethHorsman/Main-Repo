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
    POST_LENGTH = HOUSE_LENGTH - BALCONY_LENGTH
    DOOR_X = HOUSE_X + 50
    DOOR_Y = HOUSE_Y + 50
    DOOR_LENGTH = HOUSE_LENGTH - 50
    WINDOW_X = HOUSE_X + 195
    WINDOW_Y = HOUSE_Y + 70
    WINDOW_WIDTH = 120
    WINDOW_LENGTH = 80
    WINDOW_CENTER_VER = WINDOW_Y + (WINDOW_LENGTH / 2)
    WINDOW_CENTER_HOR = WINDOW_X + (WINDOW_WIDTH / 2)


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
    polygon(0,580, 50,550, 475,550, 435,600, 0,600) ## house shadow
    # polygon(bottom left corner, top left corner, top right corner, bottom right corner, lower bottom left corner)

    setFill(85,105,45)
    polygon(390,560, 445,560, 410,600, 350,600) ## gap in house shadow


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
    rect(HOUSE_X+POST_WIDTH,HOUSE_Y+5,  HOUSE_WIDTH-POST_WIDTH, 5) ## roof shadow
    rect(200,350,7,185) ## vertical door shadow
    rect(100,345,107,7) ## horizontal door shadow
    rect(365,370,5,82) ## vertical window shadow
    rect(245,365,125,5) ## horiztonal window shadow

    setOutline(150,135,110)
    setFill(150,135,110)
    rect(HOUSE_X+HOUSE_WIDTH,HOUSE_Y,  5, HOUSE_LENGTH) ## right wall highlight

    # ROOF
    setOutline(80, 80, 80)
    setFill(70, 70, 70)
    polygon(ROOF_LEFT,HOUSE_Y,  ROOF_RIGHT,HOUSE_Y,  ROOF_RIGHT-150,ROOF_TOP,  ROOF_LEFT+125,ROOF_TOP)
    # polygon(bottom left corner, bottom right corner, top right corner, top left corner)

    setOutline(60,60,60)
    line_height = HOUSE_Y - 10
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
    setOutline(10,10,10) # Black is (0,0,0)
    setFill(40, 40, 40)
    rect(DOOR_X,DOOR_Y, 100, DOOR_LENGTH) ## base from (100,350) to (200,535)

    setOutline(38,38,38)
    setFill(37,37,37)
    rect(DOOR_X+10,DOOR_Y+15, 35, 80) # upper left indent outline
    rect(DOOR_X+55,DOOR_Y+15, 35, 80) # upper right indent outilne
    rect(DOOR_X+10,DOOR_Y+100, 80, 75) # bottom indent outline

    setOutline(36,36,36)
    setFill(35,35,35)
    rect(DOOR_X+15,DOOR_Y+20, 25, 70) # upper left indent
    rect(DOOR_X+60,DOOR_Y+20, 25, 70) # upper right indent
    rect(DOOR_X+15,DOOR_Y+105, 70, 65) # bottom indent

    setOutline(100,60,20) # tan4 is (139,90,43)
    setFill(80, 55, 40)
    ellipse(DOOR_X+85,DOOR_Y+90, 10, 10) ## knob


    # WINDOW
    setOutline(30, 30, 30)
    setFill(205, 200, 115) # khaki3 is (205,198,115)
    rect(WINDOW_X,WINDOW_Y, WINDOW_WIDTH, WINDOW_LENGTH) ## base from (245,370) to (365,450)

    setOutline(210, 205, 120)
    setFill(215, 210, 125)
    polygon(WINDOW_X+1,411, WINDOW_X+1,448, 286,448, 363,409, 363,371, 324,371) # highlight
    # polygon(bottom upper, bottom corner, bottom right, top lower, top corner, top left)
    
    setOutline(30, 30, 30)
    line(WINDOW_X,WINDOW_CENTER_VER,  WINDOW_X+WINDOW_WIDTH,WINDOW_CENTER_VER) ## horizontal line
    line(WINDOW_CENTER_HOR,WINDOW_Y,  WINDOW_CENTER_HOR,WINDOW_Y+WINDOW_LENGTH) ## vertical line


    # MY KITTY!
    setOutline(50,50,50)
    setFill(50,50,50)
    polygon(331,447, 339,444, 330,440) ## left ear
    polygon(344,447, 336,444, 345,440) ## right ear
    pieSlice(324,447, 5, 3, 0, 180) ## left paw
    pieSlice(347,447, 5, 3, 0, 180) ## right paw
    pieSlice(330,442, 15,14, 0, 180) ## head

    setOutline(120,120,120)
    blob(336,449, 336,448, 337,449, 338,450, 339,448, 337,449) ## moustache

    setFill(150,100,75)
    ellipse(334,445, 2, 2) ## left eye
    ellipse(340,445, 2, 2) ## right eye

    setOutline(30,30,30)
    line(245,450, 365,450) ## thickened windowsill to cover moustache pixel


    # BALCONY
    setOutline("azure4") # (131,139,139)
    setFill("azure4")
    rect(50,535, 425, 15) ## base from (50,535) to (475,550)

    setFill(125,135,135)
    rect(65,530, 330, 5) ## shadow

    setFill(135,145,145)
    rect(395,530, 65, 5) ## highlight


    # BALCONY POSTS
    setOutline("burlywood4") # (139,115,85)
    setFill(140,115,85)
    rect(50,301, 15, 235) ## left post
    rect(460,301, 15, 235) ## right post
    rect(50,301, 425, 5) ## horizonal post

    setOutline(155,130,100)
    line(65,310, 65,535) ## left post highlight
    line(474,301, 474,535) ## right post highilght


    # BENCH
    setOutline(110,85,55)
    setFill(110,85,55)
    rect(250,500, 110, 10) ## bench seat
    rect(250,510, 10, 22) ## left leg
    rect(350,510, 10, 22) ## right leg

    setOutline(95,70,40)
    line(249,500, 249,532) ## left leg shadow
    line(349,510, 349,532) ## right leg shadow

    # NAME
    setOutline("black")
    setFont("montserratsemibold","8.5")
    text(5, 590, "Made by Kenneth Horsman", "w")

if __name__=="__main__":
    main()