'''Create a program that draws a house similar to the one shown below using the SimpleGraphics module
available on the course website.
While you are free to take some artistic license while creating your image, you must include the sky and
ground, a cloud, the sun, and a house with a door, window and roof that are all different colors. Include
your name in the lower right corner of the image.
'''

from SimpleGraphics import *

def main():
    # SKY BACKGROUND
    setOutline(244, 160, 175)
    setFill(244, 160, 175)
    rect(0,0, 800, 100) # top

    setOutline(246, 155, 170)
    setFill(246, 155, 170)
    rect(0,100, 800, 100)

    setOutline(248, 150, 165)
    setFill(248, 150, 165)
    rect(0,200, 800, 75)

    setOutline(250, 145, 160)
    setFill(250, 145, 160)
    rect(0,275, 800, 125) # bottom

    # SUN
    setOutline(255, 205, 0)
    setFill(255, 205, 0)
    ellipse(595, 295, 85, 85) # outer edge

    setOutline(255, 210, 0)
    setFill(255, 210, 0)
    ellipse(600, 300, 75, 75) # inner circle

    # CLOUDS
    setOutline("thistle3")
    setFill("thistle3")
    blob(725,125, 575,125, 650,135, 700,95) # bottom of upper right
    blob(650,50, 700,100, 545,80, 750,75, 675,125, 575,90, 625,95) # upper right
    blob(500,125, 425,120, 500,140, 350,130) # middle
    blob(50,80, 250,100, 275,75, 400, 90) # top left
    blob(550, 210, 600,200, 700,220, 750, 210, 775, 210, 575,175, 800, 180, 650, 225) # just above sun
    blob(20, 210, 60, 220, 70, 230, 160, 215) # left of house

    setFill(205, 180, 205)
    blob(500,310, 550,320, 600,300, 650, 310, 700,300, 630,310, 555,315, 640,330) # over sun

    # GRASS
    setOutline("dark olive green")
    setFill(85, 105, 45)
    rect(0, 400, 800, 200)

    setFill(80, 100, 40)
    ellipse(0, 399, 100, 10) # just left of house
    ellipse(300, 398, 250, 22) # just right of house
    ellipse(500, 399, 225, 10) # under sun
    ellipse(640, 395, 300, 20) # right edge

    setFill(75, 95, 35)
    polygon(0,580, 50,550, 475,550, 425,600, 0,600)

    # POND
    setOutline("bisque3")
    setFill("bisque3")
    blob(900,400, 690,400, 675,450, 700,500, 675,600, 700,700) # sand

    setOutline("light steel blue")
    setFill(170,190,220)
    blob(900,410, 725,400, 700,450, 725,500, 725,600, 900,700) # highlight

    setFill("light steel blue")
    blob(715,460, 720,410, 825,415, 900,550, 850,700, 800,700, 750,600, 760,500)

    # BASE OF ROOF
    setOutline(90, 90, 90)
    setFill(90, 90, 90)
    polygon(25,300, 500,300, 350,175, 150,175, 25,300)

    # ROOF LINES
    setOutline(80,80,80)
    roof_top = 175
    line_height = 290
    line_start = 35
    line_end = 490
    while line_height >= roof_top:
        line(line_start, line_height, line_end, line_height)
        line_start += 15
        line_end -= 18
        line_height -= 15

    # BASE OF HOUSE
    setOutline("wheat4")
    setFill(145, 130, 105)
    rect(50, 300, 350, 250) # (50,300) to (400, 550) - use this for CONST's?

    # BALCONY POSTS
    setOutline("burlywood4")
    setFill(140, 115, 85)
    rect(50, 300, 15, 250) # left post
    rect(460, 300, 15, 250) # right post
    rect(50, 300, 425, 5) # top post

    # BASE OF BALCONY
    setOutline("azure4")
    setFill("azure4")
    rect(50, 535, 425, 15)

    # DOOR
    setOutline("Black")
    setFill(30, 30, 30)
    rect(100, 350, 100, 185) # base of door

    setFill(26, 26, 26)
    rect(110, 365, 37, 80) # upper left indent
    rect(153, 365, 37, 80) # upper right indent
    rect(110, 450, 80, 75) # bottom indent

    setOutline("tan4")
    setFill(90, 65, 50)
    ellipse(185, 440, 10, 10) # knob

    # WINDOW
    setOutline(30, 30, 30)
    setFill(205, 200, 115)
    rect(245, 370, 120, 80) # base

    setOutline(210, 205, 120)
    setFill(215, 210, 125)
    polygon(246,411, 246,448, 286,448, 363,409, 363,371, 324,371, 246,411) # highlight
    
    setOutline(30, 30, 30)
    line(245, 410, 365, 410) # horizontal line
    line(305, 370, 305, 450) # vertical line

    # Name
    setFont("Times","8", "bold")
    text(5, 590, "Made by Kenneth Horsman", "w")

if __name__=="__main__":
    main()