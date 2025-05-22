'''
Kenneth Horsman (UCID: 30260797)

Requirements for the Curving Square illusion:
 Resize the window so that it is 512 pixels by 512 pixels by calling the resize function.
 Clear the window so that any previous illusion is removed and the background is white by
calling the clear function.
 Draw 20 concentric rings that are evenly space and fill the window. The diameter of each
ring is 35 pixels larger than the next smaller ring.
 The widths of the rings should vary from 1 to approximately 7 pixels, with the narrower rings
appearing toward the middle of the image.
 The rings should be drawn in dark gray (r: 64, g: 64, b: 64).
 The squares should be centered in the window with widths of 128, 256 and 384 pixels.
 The inner square should have a line width of 2, the middle square a line width of 3, and the
outer square a line width of 4.
 The squares should be drawn in a dark purple color. 
'''

from SimpleGraphics import *

resize(512,512)
background("white")
clear()

num_rings = 20
curr_line_width = 1
curr_diameter = 15
circ_x = 256 - (curr_diameter / 2)
circ_y = 256 - (curr_diameter / 2)

setOutline(64,64,64); setFill(255,255,255)
while num_rings > 0:
    setWidth(curr_line_width)
    arc(circ_x,circ_y, curr_diameter, curr_diameter, 0,359.99999) # If I put 360, nothing is displayed
    curr_diameter += 35
    circ_x -= 17.5 # half of 3
    circ_y -= 17.5
    curr_line_width *= 1.1 # Ending line width will be just over 6.7
    num_rings -= 1

num_squares = 3
curr_line_width = 4
square_offset = 384 / 2

setOutline(60,0,80)
while num_squares > 0:
    setWidth(curr_line_width)
    line(256-square_offset, 256-square_offset, # top left
         256+square_offset, 256-square_offset, # top right
         256+square_offset, 256+square_offset, # bottom right
         256-square_offset, 256+square_offset, # bottom left 
         256-square_offset, 256-square_offset) # top left
    square_offset -= 64 # half of distance between 384, 256, and 128
    curr_line_width -= 1
    num_squares -= 1