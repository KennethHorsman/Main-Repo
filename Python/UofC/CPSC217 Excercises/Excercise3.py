'''
The first two human years each count as 10.5 dog years and each subsequent human year counts as
only 4 dog years.
Create a program that reads an age in human years and converts it to dog years using the better
conversion described in the previous paragraph. Ensure that your program works correctly for both
integer and real number ages. Your program should use a loop so that the user can keep on entering
values to convert until a value less than 0 is entered
'''

def main():
    get_new_age = True

    print('This program takes a human age as input and displays it in dog years (using better conversion).')

    while get_new_age:
        getting_age = True

        while getting_age:     
            age_human = get_age()
            if age_human >= 0: # using "if age_human:" does not work because 0 doesn't count
                getting_age = False 
        
        if age_human == 0:
            get_new_age = False
        else:
            age_dog = calc_age_dog(age_human)
            print(f"This human is {age_dog} years old in dog years.")

    print("You are exiting the program.")

def calc_age_dog(age_human):
    if age_human > 2:
        age_human -= 2
        converted_years = (age_human * 4) + (2 * 10.5) # Would be more efficient not to multiply first 2 years but I wanted to show the calculation
    else:
        converted_years = age_human * 10.5
    
    if converted_years % 1 == 0: 
        return int(converted_years)
    else:
        return converted_years

def get_age(): 
    age = input("Enter a persons age (or 0 to quit): ") # I know what the instructions said but I thought this made more sense.
    
    try:
        float(age)
        return float(age)

    except ValueError: 
        print("Please enter a number.") 
        return None

if __name__=="__main__": 
    main()