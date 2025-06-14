import tkinter
import SimpleGraphics

"""
Kenneth Horsman (UCID: 30260797)
"""

# load image object
# draw image
# if error, tkinter tclerror exception raised with error message and quit
# make sure to close every opened file
# each func needs description and parameters and result
# use constants where helpful and do NOT ever use break or continue


# test using PNG ideally or PPM if this doesnt work
# hexadecimal conversation can be done b %x to indicated integer should be in base 16, or %02x to account for leading 0
# concatenate strings when constructing character sequences needed for some/all of the pixel types

# create encoding function with image and name of new file

# get width
# get height

# get prev pixel
# list of seen colors

# for each pixel in the image
# get pixel function with getred etc?????

# write okti
# write width and height
# each line is a pixel reference, starting upper left and ending lower right, moving left to right

# ORDER:
# IF color matches prev pixel, use a run if one or more copies of the prev pixel
# IF color matches one of prev encountered pixels, use one of those
# IF difference is sufficiently small, use rgb difference method
# IF none, use full set of RGB values

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