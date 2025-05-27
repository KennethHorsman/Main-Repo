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
clear()

SQ_SIZE = 50 # The width / height of each square
CIRC_DIAMETER = 12
CIRC_OFFSET = 2 + (CIRC_DIAMETER / 2) # The center of each circle + 2 pixels from the edge of the square

CIRC_TOPLEFT = [CIRC_OFFSET, CIRC_OFFSET] # [x, y] of circle center in each square
CIRC_TOPRIGHT = [SQ_SIZE-CIRC_OFFSET, CIRC_OFFSET] # LISTS NOT ALLOWED THO
CIRC__BOTTOMLEFT = [CIRC_OFFSET, SQ_SIZE-CIRC_OFFSET]

input_row = 5
input_col = 8

# SQUARES


# UPPER LEFT SECTOR
for x in range(0,input_row):
    for y in range(0,input_col):
        print('')