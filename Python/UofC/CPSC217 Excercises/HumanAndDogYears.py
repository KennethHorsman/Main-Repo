'''
Create a program that reads a persons name and age. Display the persons name and age, along with
their age in dog years as part of the output message. Multiply a persons age by 7 to determine the age
in dog years. Ensure that your program works correctly for both integer and real number ages. 
'''

def main():
    getting_age = True

    while getting_age:    
        get_age()

def get_age():

        print('This program...')
        age = input("Enter the persons age: ")
        
        try:
            float(age)

        except ValueError:
            print("Please enter a number.")


if __name__=="__main__": # Instead of calling all the functions in the main program, I use this and only call main()
    main()