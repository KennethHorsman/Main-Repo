from SimpleGraphics import *
import _tkinter
import math # It doesn't say we cant!

import os
os.chdir(os.path.dirname(__file__))  # changes cwd to the script’s folder

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
    input_file = "differences_small.ppm"

    try:
        image = loadImage(input_file)
        drawImage(image, 0, 0)
    except _tkinter.TclError:
        print("Error: File unsupported or not found. Please try a diffferent file.")
        close()
    except:
        print("Unknown error. Please try again.")
        close()

    encodeOKTI(image, output_name)

    print("output.okti successfully created.")

    return

def encodeOKTI(image, fname):
    WIDTH = getWidth(image)
    HEIGHT = getHeight(image)
    seen_colors = [(0,0,0)]
    prev_pixel = (0,0,0)
    x = 0; y = 0

    with open(fname, "w") as file: # Automatically closes when done
        file.write("okti\n")
        file.write(f"{WIDTH} {HEIGHT}\n")

        while y < HEIGHT: # starting at top row and going left to right
            while x < WIDTH:
                pixel = getPixel(image, x, y)

                method = determineMethod(pixel, seen_colors, prev_pixel)

                match method:
                    case 1:
                        'def prev color'
                    case 2:
                        'def seen color'
                    case 3:
                        newline = smallDifference(pixel, prev_pixel)
                    case 4:
                        newline = fullRGB(pixel)
                    
                file.write(f"{newline}\n")
                x += 1
            y += 1
            x = 0

def determineMethod(pixel, seen_colors, prev_pixel):
    red, green, blue = unpackRGB(pixel)
    prev_red, prev_green, prev_blue = unpackRGB(prev_pixel)

    if pixel == prev_pixel:
        return 1
    elif pixel in seen_colors:
        return 2
    elif (-8 <= (red - prev_red) <= 7 and # because f - 8 = 7, but 0 - 8 = -8
        -8 <= (green - prev_green) <= 7 and
        -8 <= (blue - prev_blue) <= 7):
        return 3
    else:
        return 4

def fullRGB(pixel):
    red, green, blue = unpackRGB(pixel)

    red_hex = "%02x" % red
    green_hex = "%02x" % green
    blue_hex = "%02x" % blue

    newline = f"p{red_hex}{green_hex}{blue_hex}"
    return newline

def smallDifference(pixel, prev_pixel):
    red, green, blue = unpackRGB(pixel)
    prev_red, prev_green, prev_blue = unpackRGB(prev_pixel)

    diff_red = "%x" % ((red - prev_red) + 8) # 42 - 50 = -8 and +8 turns into 0 (0 - 8 = -8)
    diff_green = "%x" % ((green - prev_green) + 8) # 57 - 50 = 7 and +8 turns into f/15 (f - 8 = 7)
    diff_blue = "%x" % ((blue - prev_blue) + 8) # 46 - 50 = -4 and +8 turns into 4 (4 - 8 = -4)

    newline = f"d{diff_red}{diff_green}{diff_blue}"
    return newline

def unpackRGB(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    return (red, green, blue)

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