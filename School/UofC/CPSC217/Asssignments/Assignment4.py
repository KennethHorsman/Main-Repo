
# load image object
# draw image
# if error, tkinter tclerror exception raised with error message and quit

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

# ORDER:
# IF color matches prev pixel, use a run if one or more copies of the prev pixel
# IF color matches one of prev encountered pixels, use one of those
# IF difference is sufficiently small, use rgb difference method
# IF none, use full set of RGB values

# use while loop instead of for loop
# intitalize variables that represent x and y ahead of the loop
# body of loop increases the pixels 
# not sure how a run works because it may skip forward??

# if command line arg provided, that will be the name
# if no cmd line, read name with input function
# else, too many args provided and quit??

