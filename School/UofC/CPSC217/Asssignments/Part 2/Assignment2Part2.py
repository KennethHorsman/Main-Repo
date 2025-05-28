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

    SQUARE_SIZE = (512 - (7 * 10) - (2 * 5)) // 8
    CIRC_DIAMETER = 12
    LINE_SIZE = 10

    setOutline(128,128,128)
    DrawLines(9, "vertical", SQUARE_SIZE, LINE_SIZE)
    DrawLines(9, "horizontal", SQUARE_SIZE, LINE_SIZE) 
    
    setColor("white")
    HG_DrawCircles(CIRC_DIAMETER, SQUARE_SIZE, LINE_SIZE)

def DrawLines(num_lines, type, square_size, line_size):
    x1 = y1 = x2 = y2 = 0 # Setting all of these to 0 and updating them as required later

    while num_lines > 0:
        if num_lines == 1 or num_lines == 9:
            curr_line_size = line_size / 2
        else:
            curr_line_size = line_size

        width_os = curr_line_size / 2 # width offset is required because otherwise only half the line would show around the edges
        setWidth(curr_line_size) # Also, in the example, the top and left borders are half cut off but I kept mine symmetrical 

        if type == "vertical":
            y2 = 512
            line(x1+width_os,y1, x2+width_os,y2)

            x1 += curr_line_size + square_size # [512 - (7*10) - (2*5)] / 8 = SQ_SIZE. The 8 represents the number of squares.
            x2 += curr_line_size + square_size
            
        else:
            x2 = 512
            line(x1,y1+width_os, x2,y2+width_os)

            y1 += curr_line_size + square_size
            y2 += curr_line_size + square_size

        num_lines -= 1

def HG_DrawCircles(diameter, square_size, line_size):
    # Draws circles for the Hermann Grid illusion

    x_value = y_value = square_size + (line_size / 2) # Dividing the line size by 2 because the outer lines are half the width
    num_rows = getHeight() // square_size
    num_cols = getWidth() // square_size

    for row in range(num_rows-1): # The -1 is needed to prevent drawing onto the bottom or rightmost lines
        for col in range(num_cols-1): 

            ellipse(x_value, y_value, diameter, diameter)
            x_value += square_size + line_size

        x_value = square_size + (line_size / 2) # resets the x value to start at the beginning of the row
        y_value += square_size # moves the y value down the next row

HermannGrid()