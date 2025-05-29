import importlib
from SimpleGraphics import *
'''
Kenneth Horsman (UCID: 30260797)

'''

def main():
    getting_selection = True

    print("The following program allows you")

    print("List of Illusions:\n" \
          "1. Curving Squares Illusion\n" \
          "2. Hermann Grid Illusion\n" \
          "3. Cafe Wall Illusion\n" \
          "4. Bulging Checkerboard Illusion\n" \
          "0. Exit Program")

    while getting_selection:
        selection = getInteger("\nPlease choose an option from the above list of illusions: ", 0, 4)

        if closed():
            importlib.reload()

        match selection:
            case 1:
                print("\nCurving Squares is now being displayed.")
                Curving_Squares()
            case 2:
                print("\nHermann Grid is now being displayed.")
                HermannGrid()
            case 3:
                print("\nCafe Wall is now being displayed.")
                CafeWall()
            case 4:
                print("\nBulging Checkerboard will be displayed after your input.")
                Bulging_Checkerboard()
            case 0:
                print("\nYou have exited the program.")
                getting_selection = False # I could have just put close() here instead
    
    close()

def getInteger(message, minimum, maximum):
    getting_input = True
    while getting_input:
        user_input = input(message)
        try:
            int(user_input) # I actually don't know why this worked perfectly because you CAN turn a float into an integer??
            if int(user_input) >= minimum and int(user_input) <= maximum:
                return int(user_input) # I could have done getting_input = False and set this line below the while loop
            else:
                print(f"\nError: Please enter a number between {minimum} and {maximum}.")
        except:
            print("\nError: Please enter a whole number.")

def Curving_Squares():
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
def HermannGrid():
    resize(512,512)
    background("black") # only works when called before clear
    clear()
    SQUARE_SIZE = (512 - (7 * 10) - (2 * 5)) // 8
    CIRC_DIAMETER = 11 # Diameter 12 circles do not look the same as in the example and are too big for a size 10 line
    LINE_SIZE = 10
    setOutline(128,128,128)
    HG_DrawLines(9, "vertical", SQUARE_SIZE, LINE_SIZE)
    HG_DrawLines(9, "horizontal", SQUARE_SIZE, LINE_SIZE) 
    setColor("white")
    HG_DrawCircles(CIRC_DIAMETER, SQUARE_SIZE, LINE_SIZE)
def HG_DrawLines(num_lines, type, square_size, line_size):
    x1 = y1 = x2 = y2 = 0 # Setting all of these to 0 and updating them as required later
    while num_lines > 0:
        if num_lines == 1 or num_lines == 9:
            curr_line_size = line_size / 2
        else:
            curr_line_size = line_size
        width_os = curr_line_size / 2 # width offset is required because otherwise only half the line would show around the edges
        setWidth(curr_line_size) # Also, in the example, the top and left borders are half cut off but I kept mine symmetrical 
        if type == "vertical":
            y2 = 512 # change to get width?
            line(x1+width_os,y1, x2+width_os,y2)
            x1 += curr_line_size + square_size # [512 - (7*10) - (2*5)] / 8 = SQ_SIZE. The 8 represents the number of squares.
            x2 += curr_line_size + square_size
        else:
            x2 = 512
            line(x1,y1+width_os, x2,y2+width_os)
            y1 += curr_line_size + square_size
            y2 += curr_line_size + square_size
        num_lines -= 1
def HG_DrawCircles(diameter, square_size, line_size):
    # Draws circles for the Hermann Grid illusion
    x_value = y_value = square_size + (line_size / 2) # Dividing the line size by 2 because the outer lines are half the width
    num_rows = getHeight() // square_size
    num_cols = getWidth() // square_size
    for row in range(num_rows-2): # Not including the outermost lines
        for col in range(num_cols-2): # 
            ellipse(x_value, y_value, diameter, diameter)
            x_value += square_size + line_size
        x_value = square_size + (line_size / 2) # resets the x value to start at the beginning of the row
        y_value += square_size + line_size # moves the y value down the next row
def CafeWall():
    resize(800,598) 
    background("black")
    clear()
    num_rows = int(598 / 44) # This only works because the thickness of all the lines added up is less than one square size
    curr_y = 1 # to show half of the line width at the top
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
            rect(offset,curr_y, SQ_SIZE, SQ_SIZE) # Can we not consolidate this into drawsquares?
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
def DrawSquares(x_value, y_value, square_size, line_size=0):
        # Draws one row of squares for the purposes of making a checkerboard pattern
        num_squares = int(getWidth() / square_size) / 2
        while num_squares > 0:
                rect(x_value,y_value, square_size, square_size)
                x_value += (square_size * 2) + (line_size / 2)
                num_squares -= 1
if __name__=="__main__":
    main()