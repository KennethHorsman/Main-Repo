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

from SimpleGraphics import *

def main():

    resize(800,600)
    background("white")
    clear()

    SQ_SIZE = 50
    CIRC_DIAMETER = 12
    CIRC_OFFSET = 2
    ROWS = getHeight() // SQ_SIZE # Results in 12
    COLS = getWidth() // SQ_SIZE # Results in 16

    CIRCLES_DICT = {"UPPERLEFT" : ("BOTTOMLEFT", "TOPRIGHT"),
                    "UPPERRIGHT" : ("TOPLEFT", "BOTTOMRIGHT"),
                    "LOWERLEFT" : ("TOPLEFT", "BOTTOMRIGHT"),
                    "LOWERRIGHT" : ("TOPRIGHT", "BOTTOMLEFT"),
                    "ABOVE" : ("BOTTOMLEFT", "BOTTOMRIGHT"),
                    "RIGHT" : ("TOPLEFT", "BOTTOMLEFT"),
                    "BELOW" : ("TOPLEFT", "TOPRIGHT"),
                    "LEFT" : ("TOPRIGHT", "BOTTOMRIGHT")}

    input_row = getInteger(f"Please enter the target row (between 0 and {ROWS-1}): ", 0, ROWS-1) + 1 # The +- 1 is due to the starting row/col being considered 0.
    input_col = getInteger(f"Please enter the target column (between 0 and {COLS-1}): ", 0, COLS-1) + 1

    ### SQUARES ###
    setColor("black")
    starting_y = 0
    rows = ROWS 

    while rows > 0:
        if rows % 2 == 1:
            DrawSquares(SQ_SIZE, starting_y, SQ_SIZE)
        else:
            DrawSquares(0, starting_y, SQ_SIZE)
        rows -= 1
        starting_y += SQ_SIZE


    ### CIRCLES ###
    near_side = CIRC_OFFSET
    far_side = SQ_SIZE - CIRC_OFFSET - CIRC_DIAMETER

    for key, value in CIRCLES_DICT.items():
         for corner in value:
            
            match corner: # Sets circle offsets based on the corner
                case "TOPLEFT":
                    x_offset = near_side
                    y_offset = near_side
                case "TOPRIGHT":
                    x_offset = far_side
                    y_offset = near_side
                case "BOTTOMLEFT":
                    x_offset = near_side
                    y_offset = far_side
                case "BOTTOMRIGHT":
                    x_offset = far_side
                    y_offset = far_side

            match key: # Sets starting and ending rows/columns based on the sector
                case "UPPERLEFT":
                    start_row = 0; end_row = input_row - 1
                    start_col = 0;  end_col = input_col - 1            
                case "UPPERRIGHT":
                    start_row = 0; end_row = input_row - 1
                    start_col = input_col + 1;  end_col = COLS  
                case "LOWERLEFT":
                    start_row = input_row + 1; end_row = ROWS
                    start_col = 0;  end_col = input_col - 1
                case "LOWERRIGHT":
                    start_row = input_row + 1; end_row = ROWS
                    start_col = input_col + 1;  end_col = COLS
                case "ABOVE":
                    start_row = 0; end_row = input_row - 1;
                    start_col = input_col; end_col = input_col
                case "RIGHT":
                    start_row = input_row; end_row = input_row
                    start_col = input_col + 1; end_col = COLS
                case "BELOW":
                    start_row = input_row + 1; end_row = ROWS
                    start_col = input_col; end_col = input_col
                case "LEFT":
                    start_row = input_row; end_row = input_row
                    start_col = 0; end_col = input_col - 1
                
            BC_DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, CIRC_DIAMETER, SQ_SIZE)

def DrawSquares(x_value, y_value, square_size, line_size=0):
        # Draws one row of squares for the purposes of making a checkerboard pattern

        num_squares = int(getWidth() / square_size) / 2
        
        while num_squares > 0:
                rect(x_value,y_value, square_size, square_size)

                x_value += (square_size * 2) + (line_size / 2)
                num_squares -= 1

def BC_DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, diameter, square_size):
    # Draws circles within the specified squares for the bulging checkerboard illusion

    x_value = x_offset + ((start_col-1) * square_size) # Corner offset plus the number of cols before this column
    y_value = y_offset + ((start_row-1) * square_size)

    for row in range(start_row, end_row+1): # Range function does not include the last value
        for col in range(start_col, end_col+1): 
            
            if row % 2 == 0:
                if col % 2 == 0:
                    setColor("white")
                else:
                    setColor("black")
            else:
                if col % 2 == 0:
                    setColor("black")
                else:
                    setColor("white")

            ellipse(x_value, y_value, diameter, diameter)
            x_value += square_size

        x_value = x_offset + ((start_col-1) * square_size) # resets the x value to start at the beginning of the row
        y_value += square_size # moves the y value down the next row

def getInteger(message, minimum, maximum):
    getting_input = True

    while getting_input:
        user_input = input(message)

        try:
            int(user_input) # I actually don't know why this worked perfectly because you CAN turn a float into an integer??

            if int(user_input) > minimum and int(user_input) < maximum:
                return int(user_input) # I could have done getting_input = False and set this line below the while loop
            else:
                print(f"Error: Please enter a number between {minimum} and {maximum}.")
                
        except:
            print("Error: Please enter a whole number.")


if __name__=="__main__":
    main()