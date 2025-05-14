'''
Kenneth Horsman (UCID: 30260797)

Create a program that reads a persons name and age. Display the persons name and age, along with
their age in dog years as part of the output message. Multiply a persons age by 7 to determine the age
in dog years. Ensure that your program works correctly for both integer and real number ages. 
'''

def main():
    getting_age = True # sentinel used to determine loop status

    print("This program determines how old a person is in dog years.")

    name = input("Enter the persons name: ")

    while getting_age:     
        age_human = get_age()
        if age_human: # if the value returned was not None...
            getting_age = False # exit loop

    age_dog = age_human * 7

    print(f"{name} is {age_human} in human years and {age_dog} in dog years.")
    
    if age_human > 120:
        print(f"Is {name} a vampire?")

def get_age(): # Good practice to create functions for a singular purpose
    age = input("Enter the persons age: ")
    
    try:
        float(age) # attempts to convert the string into a float (numbers / periods only)
        if float(age) % 1 == 0: # if successful, determines if the number is whole or not by whether there's any remainder
            return int(age)
        else:
            return float(age)

    except ValueError: # This is the error that occurs when the value entered is not a numer or a period
        print("Please enter a number.") # I am not using raise() so I can return None and continue loop in main()
        return None

if __name__=="__main__": # By only calling main(), I can organize my code top-down
    main()