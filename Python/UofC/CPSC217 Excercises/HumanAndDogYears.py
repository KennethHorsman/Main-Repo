'''
Create a program that reads a persons name and age. Display the persons name and age, along with
their age in dog years as part of the output message. Multiply a persons age by 7 to determine the age
in dog years. Ensure that your program works correctly for both integer and real number ages. 
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