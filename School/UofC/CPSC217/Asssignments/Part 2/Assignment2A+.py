'''
Kenneth Horsman (UCID: 30260797)

The bulging checkerboard illusion consists of black and white squares in a checkerboard pattern,
most of which have two small dots drawn on then. While all of the black and white regions in the
board are square and have the same size, most people perceive that the board bulges at a
particular square once the small dots are added to the image.
Read the row and column numbers for the target square from the user. Then add dots to the other
squares in the following manner:
 Squares above and to the left of the target square have dots in the lower left corner and the
upper right corner.
 Squares directly above the target square have dots in the lower left corner and the lower
right corner.
 Squares above and to the right of the target square have dots in the upper left corner and
the lower right corner.
 Squares directly to the right of the target square have dots in the upper left corner and the
lower left corner.
7
 Squares below and to the right of the target square have dots in the upper right corner and
the lower left corner of the square.
 Squares directly below the target square have dots in the upper left corner and the upper
right corner.
 Squares below and to the left of the target square have dots in the upper left corner and the
lower right corner.
 Squares directly to the left of the target square have dots in the upper right corner and the
lower right corner.
 No circles are drawn in the target square.

Resize the window so that it is 800 pixels wide and 600 pixels tall. Each square in the illusion is 50
pixels by 50 pixels. Each of the circles has a diameter of 12 pixels. Each circle is 2 pixels from the
two closest edges of the square in which it resides
'''

# using square width for column and row locations with two for loops
# for all colums from x onward, for all rows in range y, use one of 4 offsets for circle (each corner, based on top or left of square border)

from SimpleGraphics import *

resize(800,600)
background("white")
clear()

SQ_SIZE = 50
CIRC_DIAMETER = 12
CIRC_OFFSET = 2
ROWS = int(getHeight() / SQ_SIZE)
COLS = int(getWidth() / SQ_SIZE)

#CIRC_TOPLEFT = [CIRC_OFFSET, CIRC_OFFSET] # [x, y] of circle center in each square
#CIRC_TOPRIGHT = [SQ_SIZE-CIRC_OFFSET, CIRC_OFFSET] # LISTS NOT ALLOWED THO
#CIRC__BOTTOMLEFT = [CIRC_OFFSET, SQ_SIZE-CIRC_OFFSET]

def DrawSquares(x_value, y_value, square_size, line_size=0):
    # Draws one row of squares
    setColor("black")

    num_squares = int(getWidth() / square_size) / 2
    
    while num_squares > 0:
            rect(x_value,y_value, square_size, square_size)

            x_value += (square_size * 2) + (line_size / 2)
            num_squares -= 1


def DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, diameter, square_size):
    # Draws circles within the specified squares
    setColor("red")

    x_value = x_offset + (start_col * square_size)
    y_value = y_offset + (start_row * square_size)

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            ellipse(x_value, y_value, diameter, diameter)
            x_value += square_size

        x_value = x_offset # resets the x value to start at the beginning of the row
        y_value += square_size # moves the y value to move down the next row

### SQUARES ###
starting_y = 0
rows = ROWS 

while rows > 0:
    if rows % 2 == 1:
        DrawSquares(SQ_SIZE, starting_y, SQ_SIZE)
    else:
        DrawSquares(0, starting_y, SQ_SIZE)
    rows -= 1
    starting_y += SQ_SIZE


input_row = 6
input_col = 8

### UPPER LEFT SECTOR ###
#start_row = 0; end_row = input_row - 1
#start_col = 0;  end_col = input_col - 1

### UPPER RIGHT SECTOR ###
start_row = 0; end_row = input_row - 1
start_col = input_col + 1;  end_col = COLS

### LOWER LEFT SECTOR ####
#start_row = input_row + 1; end_row = ROWS
#start_col = 0;  end_col = input_col - 1

### LOWER RIGHT SECTOR ###
#start_row = input_row + 1; end_row = ROWS
#start_col = input_col + 1;  end_col = COLS


# Lower left circles
x_offset = CIRC_OFFSET
y_offset = SQ_SIZE - CIRC_OFFSET - CIRC_DIAMETER
DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, CIRC_DIAMETER, SQ_SIZE)

# Upper right circles
x_offset = SQ_SIZE - CIRC_OFFSET - CIRC_DIAMETER
y_offset = CIRC_OFFSET
DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, CIRC_DIAMETER, SQ_SIZE)

# Lower right circles
x_offset = SQ_SIZE - CIRC_OFFSET - CIRC_DIAMETER
y_offset = SQ_SIZE - CIRC_OFFSET - CIRC_DIAMETER
DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, CIRC_DIAMETER, SQ_SIZE)

# Upper left circles
x_offset = CIRC_OFFSET
y_offset = CIRC_OFFSET
DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, CIRC_DIAMETER, SQ_SIZE)