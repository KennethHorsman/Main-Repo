from SimpleGraphics import *
import _tkinter
import math # It doesn't say we cant!

"""
Kenneth Horsman (UCID: 30260797)
"""

# load image object
# draw image (drawImage(img, UL x, UL y) to display the chosen file for some reason)
# if error, tkinter tclerror exception raised with error message and quit
# make sure to close every opened file
# each func needs description and parameters and result
# use constants where helpful and do NOT ever use break or continue
def main():
    output_name = "output.okti"
    image = "tiny.png"

    try:
        loadImage(image)
    except _tkinter.TclError:
        print("Error: File unsupported or not found. Please try a diffferent file.")
        close()
    except:
        print("Unknown error. Please try again.")
        close()

    drawImage(image) # No idea why we're drawing the image
    encodeOKTI(image, output_name)

    return

def encodeOKTI(image, fname):
    WIDTH = image.getWidth()
    HEIGHT = image.getHeight()
    seen_colors = [(0,0,0)]
    prev_pixel = (0,0,0)
    x = 0; y = 0

    with open(fname, "w") as file: # Automatically closes when done
        file.write("okti\n")
        file.write(f"{WIDTH} {HEIGHT}\n")

        while x <= WIDTH: # starting at top row and going left to right
            while y <= HEIGHT:
                pixel = getPixel(image, x, y)
                red, green, blue = pixel[0], pixel[1], pixel[2]

                method = determineMethod(pixel, seen_colors, prev_pixel)

                match method:
                    case 1:
                        'def prev color'
                    case 2:
                        'def seen color'
                    case 3:
                        'def difference'
                    case 4:
                        newline = fullRGB(red, green, blue)
                    
                file.write(f"{newline}\n")
                x += 1
            y += 1
            x = 0

def determineMethod(pixel, seen_colors, prev_pixel):
    if pixel == prev_pixel:
        return 1
    elif pixel in seen_colors:
        return 2
    elif math.isclose(pixel[0], prev_pixel, 7) and math.isclose(pixel[1], prev_pixel, 7) and math.isclose(pixel[2], prev_pixel, 7):
        return 3
    else:
        return 4

def fullRGB(red, green, blue):
    red_hex = "%02x" % red
    green_hex = "%02x" % green
    blue_hex = "%02x" % blue

    newline = f"p{red_hex}{green_hex}{blue_hex}"
    return newline

# test using PNG ideally or PPM if this doesnt work
# hexadecimal conversation can be done b %x to indicated integer should be in base 16, or %02x to account for leading 0
# concatenate strings when constructing character sequences needed for some/all of the pixel types

# FULL RGB
# 7 characters starting with a 'p' followed by 6 hexadecimal digits
# 2 red, 2 green, 2 blue, ranging from 0 to 255 (ff)

# DIFFERENCE
# begins with 'd' followed by 3 hexadecimal digits
# curr pixel intalized to black (0,0,0) before loading begins to allow first pixel in image to be a difference from previous 
# difference in red, green, blue where the curr pixel is 8 bits smaller than the difference
# so if you do d0f4, the curr pixel is 8 less red (0 - 8 = -8), 7 more green (f - 8 = 7), and 4 less blue (4 - 8 = -4)

# RUN
# two variations: 'r' plus single hex digit to represent number of additional copies to be included (up to 15)
# "R" with 2 hex digits that represent number of additional copies, being up to 255. Could span several rows.
# intialize to black

# COPY OF PREV
# color inserted to front of list of previous colours (initalize with black), IF NOT IN LIST ALREADY
# if length greater than 256, last color should be discarded to make room
# 'i' plus single hex, being the index into the list of prev colors
# 'I' two hex digits which ref the list of colors

# use while loop instead of for loop
# intitalize variables that represent x and y ahead of the loop
# body of loop increases the pixels 
# not sure how a run works because it may skip forward??

# if command line arg provided, that will be the name
# if no cmd line, read name with input function
# else, too many args provided and quit??

# use the tiny files first
# start with support for full RGB values
# then diff from prev pixel
# then run of identical pixels
# then list of prev pixels

# always output to output.okti
# websites or fc command can be used to check difference in files

if __name__ == "__main__":
    main()