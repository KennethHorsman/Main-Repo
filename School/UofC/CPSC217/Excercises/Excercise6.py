"""
Kenneth Horsman (UCID: 30260797)

Write a program that reads a postal code from the user and displays the name of the province in which
that postal code resides. Your program cannot include any if statements, loops or lists. As a result,
you will almost certainly want to use a dictionary to solve this problem.
Your program does not need to do any error checking. The user will always enter a 6-character postal
code that begins with one of the letters indicated in the previous table.

A program that includes an if statement, loop or list will receive a grade of F even if all of the output is correct.
"""

def main():
    print("This program takes a Canadian postal code as input and returns the associated province.")

    postal_dict = {"T" : "Alberta",
                   "V" : "British Columbia",
                   "R" : "Manitoba",
                   "E" : "New Brunswick",
                   "A" : "Newfoundland",
                   "B" : "Nova Scotia",
                   "X" : "Nunavut or the Northwest Territories",
                   **dict.fromkeys(("K","L","M","N","P"), "Ontario"),
                        # This method basically unpacks the key-value pairs in the background instead of forcing me to manually write them one by one
                        # ref: https://www.geeksforgeeks.org/python-initialize-dictionary-with-multiple-keys/ 
                   "C" : "Prince Edward Island",
                   **dict.fromkeys(("G","H","J"), "Quebec"),
                   "S" : "Saskatchewan",
                   "Y" : "Yukon"}
    
    first_digit = input("Please enter the postal code: ")[0] # takes only the first character from the input string

    print(f"That postal code is from the province of {postal_dict[first_digit]}.")

if __name__=="__main__":
    main()