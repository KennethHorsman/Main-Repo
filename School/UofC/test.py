from SimpleGraphics import *

curr_line_width = 1
curr_diameter = 15
curr_x = 256 - curr_diameter
curr_y = 256 - curr_diameter

resize(512,512)
setOutline(0,0,0)
arc(curr_x,curr_y, curr_diameter, curr_diameter, 0, 359)