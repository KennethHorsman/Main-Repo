# Cornwall.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

# Write computeRate function here
def computeRate(days,code=None):
    if code == "A":
        rate = 169.00
    elif code == "C":
        rate = 112.00
    else:
        rate = 99.99
    result = days * rate
    return result


if __name__ == '__main__':
    rate = 99.99
    dayString = input("How many days do you plan to stay? ")
    days = int(dayString)
    question = input("Do you want a meal plan? Y or N: ")

    # Figure out which arguments to pass to the computeRate() function and 
    # then call the computeRate() function
    if question == "N":
        result = computeRate(days)
        print("The rate for your stay is: " + str(result))
    elif question == "Y": 
        code = input("Enter A or C for meal plan code: ")
        result = computeRate(days,code)
        print("The rate for your stay is: " + str(result))

