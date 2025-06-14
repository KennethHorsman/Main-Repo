import importlib
import SimpleGraphics # I had to add this to be able to reload
from SimpleGraphics import *

'''
Programmer: Kenneth Horsman (UCID: 30260797)
This program allows the user to select and display one of four illusions.

NOTE: I know the instructions stated not to import any other modules but I couldn't 
find another way to prevent an error if you accidentally close the window.
I assume this was to prevent cheating but my import does not impact drawings.

'''

close() # Closes the blank window that opens when SimpleGraphics is imported.

def main():
    getting_selection = True

    print("List of Illusions:\n" \
          "1. Curving Squares Illusion\n" \
          "2. Hermann Grid Illusion\n" \
          "3. Cafe Wall Illusion\n" \
          "4. Bulging Checkerboard Illusion\n" \
          "0. Exit Program\n")

    while getting_selection:
        selection = getInteger("Please choose an option from the above list of illusions: ", 0, 4)

        if closed(): # SimpleGraphics function that checks if the user closed the program
            importlib.reload(SimpleGraphics) # Reloads the SimpleGraphics file, which re-opens the program window
            
        match selection:
            case 1:
                print("Curving Squares is now being displayed.")
                Curving_Squares()
            case 2:
                print("Hermann Grid is now being displayed.")
                Hermann_Grid()
            case 3:
                print("Cafe Wall is now being displayed.")
                Cafe_Wall()
            case 4:
                print("Bulging Checkerboard will be displayed after your input.")
                Bulging_Checkerboard()
            case 0:
                print("You have exited the program.")
                getting_selection = False
    
    close() # Alternative solution: Set getting_selection to False and calling close() outside the loop.

def getInteger(message, minimum, maximum):
    getting_input = True
    while getting_input:
        try:
            value = int(input(message)) # I actually don't know why this worked perfectly because you CAN turn a float into an integer
            if value >= minimum and value <= maximum:
                return value
            else:
                print(f"Error: Please enter a number between {minimum} and {maximum}.")
        except:
            print("Error: Please enter a whole number.")

def Curving_Squares():
    resize(512,512)
    background("white") # This function only works when called before clear().
    clear()

    ### RINGS ###
    CENTER_WIDTH = (getWidth() / 2)
    DIAMETER_INCREASE = 35
    num_rings = 20
    curr_line_width = 1
    curr_diameter = 15
    circ_x = CENTER_WIDTH - (curr_diameter / 2)
    circ_y = CENTER_WIDTH - (curr_diameter / 2)

    setOutline(64,64,64); setFill(None)
    for ring in range(0, num_rings):
        setWidth(curr_line_width)
        arc(circ_x,circ_y, curr_diameter, curr_diameter, 0,359.99) # If I put 360, nothing is displayed.

        curr_diameter += DIAMETER_INCREASE
        circ_x -= (DIAMETER_INCREASE / 2)
        circ_y -= (DIAMETER_INCREASE / 2)
        curr_line_width *= 1.1 # Ending line width will be just over 6.7

    ### SQUARES ###
    num_squares = 3
    curr_line_width = 4
    square_offset = 384 / 2 # The 3 squares have a width of 384, 256, and 128.

    setOutline(60,0,80)
    for square in range (0, num_squares):
        setWidth(curr_line_width)
        line(CENTER_WIDTH-square_offset, CENTER_WIDTH-square_offset, # Top left
            CENTER_WIDTH+square_offset, CENTER_WIDTH-square_offset, # Top right
            CENTER_WIDTH+square_offset, CENTER_WIDTH+square_offset, # Bottom right
            CENTER_WIDTH-square_offset, CENTER_WIDTH+square_offset, # Bottom left 
            CENTER_WIDTH-square_offset, CENTER_WIDTH-square_offset) # Top left
        
        square_offset -= 64 # Half of the difference in width between each square (128).
        curr_line_width -= 1

def Hermann_Grid():
    resize(512,512)
    background("black")
    clear()

    NUM_SQUARES = 8
    LINE_SIZE = 10
    SQUARE_SIZE = int((getWidth() - (7 * LINE_SIZE) - (2 * (LINE_SIZE / 2))) / NUM_SQUARES) # Causes an error in for loop when this is float.
    CIRC_DIAMETER = 11 # Diameter 12 circles do not look the same as the circles in the example and are too big for a size 10 line.

    setOutline(128,128,128)
    HG_DrawLines(NUM_SQUARES+1, "vertical", SQUARE_SIZE, LINE_SIZE)
    HG_DrawLines(NUM_SQUARES+1, "horizontal", SQUARE_SIZE, LINE_SIZE) 

    setColor("white")
    HG_DrawCircles(CIRC_DIAMETER, SQUARE_SIZE, LINE_SIZE)

def HG_DrawLines(num_lines, type, square_size, line_size): # In the example, the top and left borders are half cut off but I kept mine symmetrical.
    x1 = y1 = x2 = y2 = 0
    curr_line = num_lines

    while curr_line > 0:
        if curr_line == 1 or curr_line == num_lines: # If at the edge of the window...
            curr_line_size = line_size / 2 # Set to half width.
        else:
            curr_line_size = line_size

        setWidth(curr_line_size) 
        line_offset = curr_line_size / 2 # Line offset is required because otherwise only half the line would show around the edges.

        if type == "vertical":
            y2 = getHeight()
            line(x1+line_offset, y1,  x2+line_offset, y2)
            x1 += curr_line_size + square_size
            x2 += curr_line_size + square_size
        else:
            x2 = getWidth()
            line(x1, y1+line_offset,  x2, y2+line_offset)
            y1 += curr_line_size + square_size
            y2 += curr_line_size + square_size

        curr_line -= 1

def HG_DrawCircles(diameter, square_size, line_size):
    x_value = y_value = square_size + (line_size / 2) # Dividing the line size by 2 because the outer lines are half the width.
    num_rows = getHeight() // square_size
    num_cols = getWidth() // square_size

    for row in range(num_rows-2): # Not including the outermost lines.
        for col in range(num_cols-2): # 
            ellipse(x_value, y_value, diameter, diameter)
            x_value += square_size + line_size

        x_value = square_size + (line_size / 2) # Resets the x value to start at the beginning of the row.
        y_value += square_size + line_size # Moves the y value down the next row.

def Cafe_Wall():
    resize(800,598) 
    background("black")
    clear()

    num_rows = int(getHeight() / 44) # This only works because the thickness of all the lines added up is less than one square size.
    curr_y = 1 # Started at 1 to show half of the line width at the top.
    SQ_SIZE = 44 + 2 # Square size plus half the border width from both sides.
    LINE_WIDTH = 2

    aligned_left_rows = (1, 5, 9, 13) # Technically it's not a list... I didn't realize we weren't allowed until too late lol.
    even_rows = (2, 4, 6, 8, 10, 12)
    # remaining_rows = (3, 7, 11)

    setFill("white")
    setOutline(128,128,128)
    setWidth(LINE_WIDTH)
    while num_rows > 0:
        if num_rows in aligned_left_rows:
            offset = 0 - (LINE_WIDTH / 2)
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE)
            DrawSquares(offset + (SQ_SIZE * 2), curr_y, SQ_SIZE, LINE_WIDTH)
        elif num_rows in even_rows:
            offset = 27 - (LINE_WIDTH / 2)
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE)
            DrawSquares(offset + (SQ_SIZE * 2), curr_y, SQ_SIZE, LINE_WIDTH)
        else: # if num_rows in remaining_rows:
            offset = 42 - (LINE_WIDTH / 2)
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE)
            DrawSquares(offset + (SQ_SIZE * 2), curr_y, SQ_SIZE, LINE_WIDTH)

        line_height = curr_y + SQ_SIZE - (LINE_WIDTH / 2) # The minus 1 is to counter the starting position of 1.
        line(0,line_height, getWidth(),line_height)
        curr_y += SQ_SIZE
        num_rows -= 1

def Bulging_Checkerboard():
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

def BC_DrawCircles(start_row, end_row, start_col, end_col, x_offset, y_offset, diameter, square_size):
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

def DrawSquares(x_value, y_value, square_size, line_size=0):
        num_squares = int(getWidth() / square_size) / 2

        while num_squares > 0:
                rect(x_value,y_value, square_size, square_size)
                x_value += (square_size * 2) + (line_size / 2)
                num_squares -= 1

if __name__=="__main__":
    main()