'''
Kenneth Horsman (UCID: 30260797)
Requirements for the Café Wall Illusion:
 Resize the window so that it is 800 pixels by 598 pixels by calling the resize function.
 Clear the window so that any previous illusion is removed.
 The illusion includes 13 rows, each of which consists of alternating black and white
squares.
 Each black and white square is 44 pixels by 44 pixels. The gray lines separating the squares
are all 2 pixels wide, as are the gray lines that separate adjacent rows.
 In the first, fifth, nineth and thirteenth rows, the white square that begins the row is aligned
with the left edge of the window.
 In the even numbered rows, the first white square in the row is 27 pixels from the left edge of
the window.
 In the third, seventh and eleventh rows, the first white square is 42 pixels from the left edge
of the window. 

*Question: Is it intentional that in the example photo, the left and bottom lines are cut off?
'''

from SimpleGraphics import *

def CafeWall():

    resize(800,572) # 598 only works if I add 2 to the curr_y after each iteration, but this leaves a gap between squares. I subtracted 13 rows * 2 pixels.
    background("black")
    clear()

    num_rows = 13
    curr_y = 1 # to show half of the line width
    SQ_SIZE = 44 + 2 # square size plus half the line width from both sides
    LINE_WIDTH = 2

    aligned_left_rows = [1, 5, 9, 13]
    even_rows = [2, 4, 6, 8, 10, 12]
    # remaining_rows = [3, 7, 11]

    setFill("white")
    setOutline(128,128,128)
    setWidth(LINE_WIDTH)

    while num_rows > 0:
        if num_rows in aligned_left_rows:
            offset = 0
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE)
            DrawSquares(offset + (SQ_SIZE * 2), curr_y, SQ_SIZE, LINE_WIDTH)

        elif num_rows in even_rows:
            offset = 27 - 1
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE)
            DrawSquares(offset + (SQ_SIZE * 2), curr_y, SQ_SIZE, LINE_WIDTH)

        else: # if num_rows in remaining_rows:
            offset = 42 - 1
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE)
            DrawSquares(offset + (SQ_SIZE * 2), curr_y, SQ_SIZE, LINE_WIDTH)

        line_height = curr_y + SQ_SIZE - 1
        line(0,line_height, 800,line_height)

        curr_y += SQ_SIZE - 1
        num_rows -= 1

def DrawSquares(x_value, y_value, square_size, line_size):
    # Draws 8 squares after the first square on the left   
    num_squares = 8

    while num_squares > 0:
        rect(x_value,y_value, square_size, square_size)

        x_value += (square_size * 2) + (line_size / 2)
        num_squares -= 1

CafeWall()