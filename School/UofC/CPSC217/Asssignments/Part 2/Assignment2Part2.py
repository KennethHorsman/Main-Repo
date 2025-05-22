'''
Kenneth Horsman (UCID: 30260797)

Requirements for the Hermann Grid Illusion:
 Resize the window so that it is 512 pixels by 512 pixels by calling the resize function.
 Clear the window so that any previous illusion is removed and the background is black by
calling the clear function.
 A grid of 64 black squares is drawn, separated by gray (r: 128, g: 128, b: 128) lines. All lines
have a width of 10 pixels.
 Lines are present around the perimeter of the board (with half of the width of the 10-pixel
line outside the edge of the window).
 A white circle with a diameter of 12 pixels is drawn at the intersection of each line within the
grid (but not at the intersections around the perimeter).
Hint: There are at least two different approaches that can be taken to draw this illusion. One option
is to draw 9 gray lines that stretch all the way across the window and 9 gray lines that stretch all the
way from its top to its bottom. The other option is to draw 64 black squares that each have a gray
outline. Either approach is acceptable. The white circles are drawn after either all the lines or all of
the squares are drawn. 
'''

from SimpleGraphics import *

def HermannGrid():
    
    resize(512,512)
    background("black") # only works when called before clear
    clear()

    setOutline(128,128,128)
    DrawLines(9, "vertical")
    DrawLines(9, "horizontal") 

def DrawLines(num_lines, type):
    x1 = y1 = x2 = y2 = 0 # Setting all of these to 0 and updating them as required later

    while num_lines > 0:
        if num_lines == 1 or num_lines == 9:
            width = 5
        else:
            width = 10

        width_os = width / 2 # width offset is required because otherwise only half the line would show around the edges
        setWidth(width)

        if type == "vertical":
            y2 = 512

            line(x1+width_os,y1, x2+width_os,y2)
            x1 += width + 54 # [512 - (7*10) - (2*5)] / 8 = 54. The 8 represents the number of squares.
            x2 += width + 54
            
        else:
            x2 = 512

            line(x1,y1+width_os, x2,y2+width_os)
            y1 += width + 54
            y2 += width + 54

        num_lines -= 1

HermannGrid()