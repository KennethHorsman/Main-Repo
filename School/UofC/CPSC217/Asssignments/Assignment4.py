from SimpleGraphics import *
import _tkinter
import sys # Since we need to check for command line arguments

import os
os.chdir(os.path.dirname(__file__))  # changes cwd to the script’s folder if you're not working off root directory

"""
Kenneth Horsman (UCID: 30260797)

ENCOUNTERED PROBLEM:
1. The smallindices_small.okti file should only use p and i pixels, but it has one r pixel.

"""

def main():
    output_name = "output.okti"

    if len(sys.argv) == 2:
        input_file = sys.argv[1] # Second line of the arguments, the first being the script name
    elif len(sys.argv) > 2:
        print("Error: Too many arguments provided.")
        quit() # I could loop this error, and the below two errors, but the instructions say to quit.
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
                        newline, skips = copyColor(pixel, x, y, image, WIDTH, HEIGHT)
                        file.write(f"{newline}\n")
                        for _ in range(skips):
                            x += 1

                    case 2:
                        newline = seenColor(pixel, seen_colors)
                        file.write(f"{newline}\n")
                    case 3:
                        newline = smallDifference(pixel, prev_pixel)
                        file.write(f"{newline}\n")
                    case 4:
                        newline = fullRGB(pixel)
                        file.write(f"{newline}\n")
                        
                if pixel not in seen_colors:
                    seen_colors.insert(0, pixel)

                if len(seen_colors) > 256:
                    seen_colors.pop()

                prev_pixel = pixel
                x += 1
            y += 1
            x = 0

"""
Determines which of the four methods to use to encode a specific pixel.

Parameters:
    pixel - The current pixel to test.
    seen_colors - The list of previously seen pixels.
    prev_pixel - The previous pixel.

Returns:
    1 - Indicates a copy of the previous pixel.
    2 - Indicates a previously seen pixel.
    3 - Indicates a similar pixel to the previous one.
    4 - Indicates none of the above are applicable.
"""
def determineMethod(pixel, seen_colors, prev_pixel):
    red, green, blue = pixel
    prev_red, prev_green, prev_blue = prev_pixel

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

"""
Translates the current pixel into a full set of RGB values.

Parameters:
    pixel - The current pixel to test.

Returns:
    newline - The fully translated line to be inserted into the OKTI file.
"""
def fullRGB(pixel):
    red, green, blue = pixel

    red_hex = "%02x" % red
    green_hex = "%02x" % green
    blue_hex = "%02x" % blue

    newline = f"p{red_hex}{green_hex}{blue_hex}"
    return newline

"""
Translates the current pixel and the previous pixel into a difference of RGB values.

Parameters:
    pixel - The current pixel to test.
    prev_pixel - The previous pixel.

Returns:
    newline - The fully translated line to be inserted into the OKTI file.
"""
def smallDifference(pixel, prev_pixel):
    red, green, blue = pixel
    prev_red, prev_green, prev_blue = prev_pixel

    diff_red = "%x" % ((red - prev_red) + 8) 
    diff_green = "%x" % ((green - prev_green) + 8) 
    diff_blue = "%x" % ((blue - prev_blue) + 8)

    newline = f"d{diff_red}{diff_green}{diff_blue}"
    return newline

"""
Translates the current pixel into a full set of RGB values for the OKTI file.

Parameters:
    pixel - The current pixel to test.
    seen_colors - The list of previously seen pixels.

Returns:
    newline - The fully translated line to be inserted into the OKTI file.
"""
def seenColor(pixel, seen_colors):
    index = seen_colors.index(pixel)

    if index <= 15:
        newline = f"i{"%x" % index}"
    else:
        newline = f"I{"%02x" % index}"    
    
    return newline

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
    newline - The fully translated line to be inserted into the OKTI file.
    skips - The number of x coordinates to skip, based on the number of identical pixels.
"""
def copyColor(pixel, x, y, image, width, height):
    run = 1 # Accounting for the initial run
    temp_x = x; temp_y = y
    get_next = True

    while get_next:
        temp_x += 1

        if temp_x == width:
            temp_x = 0
            temp_y += 1 # Simulating moving to the next row

        if temp_y == height:
            get_next = False
        
        if getPixel(image, temp_x, temp_y) == pixel:
            run += 1
        else:
            get_next = False

    if run <= 15:
        newline = f"r{"%x" % run}"
    else:
        newline = f"R{"%02x" % run}"
    
    skips = run - 1
    return newline, skips

if __name__ == "__main__":
    main()