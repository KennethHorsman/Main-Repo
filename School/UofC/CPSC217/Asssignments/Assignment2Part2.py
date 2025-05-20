'''
Requirements for the Hermann Grid Illusion:
 Resize the window so that it is 512 pixels by 512 pixels by calling the resize function.
3
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