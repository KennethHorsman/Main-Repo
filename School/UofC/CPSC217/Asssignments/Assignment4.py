from SimpleGraphics import *
import _tkinter
import sys # Since we need to check for command line arguments

import os
os.chdir(os.path.dirname(__file__))  # changes cwd to the script’s folder
"""
Kenneth Horsman (UCID: 30260797)

This program takes a .png or .ppm file as input and converts it into a .okti file.

ENCOUNTERED PROBLEM:
1. The smallindices_small.okti file should only use p and i pixels, but it has one r pixel.

"""

SINGLE_HEX_MAX = 15
DOUBLE_HEX_MAX = 255
SINGLE_HEX_CONVERSION = "%x"
DOUBLE_HEX_CONVERSION = "%02x"
BIAS = 8
DIFFERENCE_MIN = -8
DIFFERENCE_MAX = 7
SEEN_COLORS_MAX = 256
LINE_MAX = 80

def main():
    output_name = "output.okti"

    if len(sys.argv) == 2:
        input_file = sys.argv[1] # Second argument, the first being the script name
    elif len(sys.argv) > 2:
        print("Error: Too many arguments provided.")
        quit()
    else:
        input_file = input("Enter a file name (including extension): ")

    try:
        image = loadImage(input_file)
        drawImage(image, 0, 0)
    except _tkinter.TclError:
        print("Error: File unsupported or not found. Please try a diffferent file.")
        close()
        quit()
    except:
        print("Unknown error. Please try again.")
        close()
        quit()

    encodeOKTI(image, output_name)

    print("output.okti successfully created.")
    quit()

"""
Encodes the provided image into OKTI format.

Paramters:
    image - the provided image to encode.
    fname - the name of the file to output to.

Returns:
    N/A
"""
def encodeOKTI(image, fname):
    SCRIPT_TYPE = 0 ### MODIFICATION: SET TO 0 FOR NORMAL, OR 1 FOR A+ ###
    WIDTH = getWidth(image)
    HEIGHT = getHeight(image)
    seen_colors = [(0,0,0)]
    prev_pixel = (0,0,0)
    x = 0; y = 0
    current_line = ""

    with open(fname, "w") as file: # Automatically closes when done
        file.write("okti\n")
        file.write(f"{WIDTH} {HEIGHT}\n")

        while y < HEIGHT: # starting at top row and going left to right
            while x < WIDTH:
                pixel = getPixel(image, x, y)

                method = determineMethod(pixel, seen_colors, prev_pixel)

                match method:
                    case 1:
                        pixel_to_write, skips = copyColor(pixel, x, y, image, WIDTH, HEIGHT)
                        for _ in range(skips):
                            x += 1
                            if x == WIDTH:
                                y += 1
                                x = 0
                    case 2:
                        pixel_to_write = seenColor(pixel, seen_colors)
                    case 3:
                        pixel_to_write = smallDifference(pixel, prev_pixel)
                    case 4:
                        pixel_to_write = fullRGB(pixel)

                if SCRIPT_TYPE == 1: ## MODIFICATION ##
                    if len((current_line + pixel_to_write)) < LINE_MAX:    
                        current_line += pixel_to_write
                    else:
                        file.write(current_line + "\n")
                        current_line = f"{pixel_to_write}"

                if SCRIPT_TYPE == 0: ## MODIFICATION ##
                    file.write(pixel_to_write + "\n")  ## MODIFICATION ##


                if pixel not in seen_colors:
                    seen_colors.insert(0, pixel)

                if len(seen_colors) > SEEN_COLORS_MAX:
                    seen_colors.pop()

                prev_pixel = pixel
                x += 1
            y += 1
            x = 0

        if SCRIPT_TYPE == 1:  ## MODIFICATION ##
            if current_line: # The last line gets skipped without adding this
                file.write(current_line + "\n")


"""
Determines which of the four methods to use to encode a specific pixel.

Parameters:
    pixel - The current pixel to test.
    seen_colors - The list of previously seen pixels.
    prev_pixel - The previous pixel.

Returns:
    1 - Indicates a copy of the previous pixel.
    2 - Indicates an already seen pixel that is not a copy of the previous pixel.
    3 - Indicates a similar pixel to the previous one, which has not been seen before.
    4 - Indicates none of the above are applicable.
"""
def determineMethod(pixel, seen_colors, prev_pixel):
    red, green, blue = pixel
    prev_red, prev_green, prev_blue = prev_pixel

    if pixel == prev_pixel:
        return 1
    elif pixel in seen_colors:
        return 2
    elif (DIFFERENCE_MIN <= (red - prev_red) <= DIFFERENCE_MAX and # f - 8 = 7, but 0 - 8 = -8
        DIFFERENCE_MIN <= (green - prev_green) <= DIFFERENCE_MAX and
        DIFFERENCE_MIN <= (blue - prev_blue) <= DIFFERENCE_MAX):
        return 3
    else:
        return 4

"""
Translates the current pixel into a full set of RGB values.

Parameters:
    pixel - The current pixel to test.

Returns:
    pixel_to_write - The fully translated line to be inserted into the OKTI file.
"""
def fullRGB(pixel):
    red, green, blue = pixel

    red_hex = DOUBLE_HEX_CONVERSION % red
    green_hex = DOUBLE_HEX_CONVERSION % green
    blue_hex = DOUBLE_HEX_CONVERSION % blue

    pixel_to_write = f"p{red_hex}{green_hex}{blue_hex}"
    return pixel_to_write

"""
Translates the current pixel and the previous pixel into a difference of RGB values.

Parameters:
    pixel - The current pixel to test.
    prev_pixel - The previous pixel.

Returns:
    pixel_to_write - The fully translated line to be inserted into the OKTI file.
"""
def smallDifference(pixel, prev_pixel):
    red, green, blue = pixel
    prev_red, prev_green, prev_blue = prev_pixel

    diff_red = SINGLE_HEX_CONVERSION % ((red - prev_red) + BIAS)
    diff_green = SINGLE_HEX_CONVERSION % ((green - prev_green) + BIAS) 
    diff_blue = SINGLE_HEX_CONVERSION % ((blue - prev_blue) + BIAS)

    pixel_to_write = f"d{diff_red}{diff_green}{diff_blue}"
    return pixel_to_write

"""
Translates the current pixel into a full set of RGB values for the OKTI file.

Parameters:
    pixel - The current pixel to test.
    seen_colors - The list of previously seen pixels.

Returns:
    pixel_to_write - The fully translated line to be inserted into the OKTI file.
"""
def seenColor(pixel, seen_colors):
    index = seen_colors.index(pixel)

    if index <= SINGLE_HEX_MAX:
        pixel_to_write = f"i{SINGLE_HEX_CONVERSION % index}"
    else:
        pixel_to_write = f"I{DOUBLE_HEX_CONVERSION % index}"    
    
    return pixel_to_write

"""
Translates the current pixel into a full set of RGB values for the OKTI file.

Parameters:
    pixel - The current pixel to test.
    x - The x position of the current pixel.
    y - The y position of the current pixel.
    image - The provided image to encode.
    width - The width of the image.
    height - The height of the image.

Returns:
    pixel_to_write - The fully translated line to be inserted into the OKTI file.
    skips - The number of x coordinates to skip, based on the number of identical pixels.
"""
def copyColor(pixel, x, y, image, width, height):
    run = 1 # Accounting for the initial run
    temp_x = x; temp_y = y
    get_next = True

    while get_next and run < DOUBLE_HEX_MAX:
        temp_x += 1

        if temp_x == width:
            temp_x = 0
            temp_y += 1 # Simulating moving to the next row

        if temp_y == height:
            get_next = False
        elif getPixel(image, temp_x, temp_y) == pixel:
            run += 1
        else:
            get_next = False

    if run <= SINGLE_HEX_MAX:
        pixel_to_write = f"r{SINGLE_HEX_CONVERSION % run}"
    else:
        pixel_to_write = f"R{DOUBLE_HEX_CONVERSION % run}"
    
    skips = run - 1 # Subtracting 1 to account for the current line being written (5 runs = 1 written line + 4 skipped lines)
    return pixel_to_write, skips

if __name__ == "__main__":
    main()