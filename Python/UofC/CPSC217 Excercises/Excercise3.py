'''
The first two human years each count as 10.5 dog years and each subsequent human year counts as
only 4 dog years.
Create a program that reads an age in human years and converts it to dog years using the better
conversion described in the previous paragraph. Ensure that your program works correctly for both
integer and real number ages. Your program should use a loop so that the user can keep on entering
values to convert until a value less than 0 is entered
'''

def main():
    getting_age = True

    print('This program...')

    while getting_age:    
        age = get_age()
        if age:
            getting_age = False

    age_dog = age * 7

    print("Age: {:.6g}".format(age_dog)) #skipping number 5 in result and is one digit short?

    if age > 120:
        print("Is this person a vampire?")

def get_age():
    age = input("Enter the persons age: ")
    
    try:
        float(age)
        return float(age)

    except ValueError:
        print("Please enter a number.")
        return None

if __name__=="__main__": # Instead of calling all the functions in the main program, I use this and only call main()
    main()