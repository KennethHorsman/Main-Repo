from SimpleGraphics import *
# Default box is 800 x 600 pixels

background("wheat") # same as setoutline below

setOutline("red") #  setOutline(string of color name)
line(150, 300, 200, 350)
line(100, 350, 100, 250, 200, 250, 200, 300) # line(first x, first y, second x, second y, third x, third y, etc.)

setOutline(100, 100, 150) # setOutline(r, g, b)
setFill("thistle")
rect(300, 50, 200, 100) #rect(top left x, top left y, width, height)

setOutline("black")
setFill("wheat")
curve(600, 75, 600, 50, 700, 50, 700, 75, \
600, 100, 600, 150, 700, 150, 700, 100) # curve(first x, first y, second x, second y, third x, third y, etc.)

ellipse(100, 50, 100, 100) #ellipse(top left box x, top left box y, box width, box height)

polygon(300, 450, 350, 450, 500, 500, 500, 550, 450, 550, 300, 500) #polygon(x1, y1, x2, y2, x3, y3, etc.)

blob(600, 350, 600, 300, 700, 300, 700, 250, 650, 250, 650, 350) # like polygon but points are just influences to curved edge

arc(100, 450, 100, 100, 0, 270) # arc(box x, box y, box width, box height, starting angle, extent)

pieSlice(600, 450, 100, 100, 60, 60) # same as arc but adds line connecting the ends to the centre

setFont("Times", "24", "bold") # setFont(font, size, modifier(s))
text(400, 300, "Example", "w") # text(x, y, text, optional anchor)