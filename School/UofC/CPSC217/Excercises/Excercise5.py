'''
Kenneth Horsman (UCID: 30260797)

Write a program that reads a collection of values from the user. After all of the values have been read,
display all of the values in the opposite order from which they were entered, with one value appearing
on each line. The user will indicate that no further values will be entered by entering a blank line.
'''

def main():
    list_of_values = []
    getting_values = True

    print('This program takes a list of values and displays them in reverse order.')

    while getting_values:
        value = input("Enter a value (or nothing to quit): ")
        
        if value:
            list_of_values.append(value)
        else:
            getting_values = False
    
    list_of_values.reverse()
    print("Values listed in reverse order:")
    for value in list_of_values:
        print(value)

if __name__ == "__main__":
    main()

