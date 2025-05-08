'''Create a program that draws a house similar to the one shown below using the SimpleGraphics module
available on the course website.
While you are free to take some artistic license while creating your image, you must include the sky and
ground, a cloud, the sun, and a house with a door, window and roof that are all different colors. Include
your name in the lower right corner of the image.
'''

from SimpleGraphics import *

def main():
    # Sky
    setOutline(244, 160, 175)
    setFill(244, 160, 175)
    rect(0,0, 800, 100)

    setOutline(246, 155, 170)
    setFill(246, 155, 170)
    rect(0,100, 800, 100)

    setOutline(248, 150, 165)
    setFill(248, 150, 165)
    rect(0,200, 800, 75)

    setOutline(250, 145, 160)
    setFill(250, 145, 160)
    rect(0,275, 800, 125)

    # Sun
    setOutline(255, 205, 0)
    setFill(255, 205, 0)
    ellipse(595, 295, 85, 85)

    setOutline(255, 210, 0)
    setFill(255, 210, 0)
    ellipse(600, 300, 75, 75)

    # Clouds
    setOutline("thistle3")
    setFill("thistle3")
    blob(725,125, 575,125, 650,135, 700,95) # bottom of upper right
    blob(650,50, 700,100, 545,80, 750,75, 675,125, 575,90, 625,95) # upper right
    blob(500,125, 425,120, 500,140, 350,130) # middle
    blob(50,80, 250,100, 275,75, 400, 90) # top left
    blob(550, 210, 600,200, 700,220, 750, 210, 775, 210, 575,175, 800, 180, 650, 225) # just above sun
    blob(20, 210, 60, 220, 70, 230, 160, 215) # left of house

    # Grass
    setOutline("dark olive green")
    setFill("dark olive green")
    rect(0, 400, 800, 200)

    # Pond
    setOutline("bisque3")
    setFill("bisque3")
    blob(900,400, 690,400, 675,450, 700,500, 675,600, 700,700)

    setOutline("light steel blue")
    setFill("light steel blue")
    blob(900,410, 725,400, 700,450, 725,500, 725,600, 900,700)

    # Roof for house
    setOutline(90, 90, 90)
    setFill(90, 90, 90)
    polygon(25, 300, 500, 300, 350, 175, 150, 175, 25, 300)

    # Base outline for house
    setOutline("wheat4")
    setFill("wheat4")
    rect(50, 300, 350, 250) # (50,300) to (400, 550) - use this for CONST's?

    # Balcony posts
    setOutline("burlywood4")
    setFill("burlywood4")
    rect(50, 300, 15, 250) # left post
    rect(460, 300, 15, 250) # right post
    rect(50, 300, 425, 5) # top post

    # Balcony base
    setOutline("azure4")
    setFill("azure4")
    rect(50, 535, 425, 15)

    # Door
    setOutline("Black")
    setFill(30, 30, 30)
    rect(100, 350, 100, 185)

    # Door knob
    setOutline("tan4")
    setFill("tan4")
    ellipse(185, 440, 10, 10)

    # Window
    setOutline(30, 30, 30)
    setFill("khaki3")
    rect(245, 370, 120, 80)
    line(245, 410, 365, 410) # horizontal line
    line(305, 370, 305, 450)

    # Name
    setFont("Times","8", "bold")
    text(5, 590, "Made by Kenneth Horsman", "w")

if __name__=="__main__":
    main()