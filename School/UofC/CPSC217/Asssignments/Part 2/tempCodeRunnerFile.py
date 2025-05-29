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