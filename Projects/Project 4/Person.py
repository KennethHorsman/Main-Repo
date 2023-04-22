#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=inconsistent-return-statements
'''
A Person contains a first name, last name, street address, zip code, and phone number. 
The class also includes a method that sets each data field, using a series of dialog boxes and 
a display method that displays all of a Persons information on a single line at the command line on the screen.
'''

# FUNCTIONS
def getalpha(prompt):
    'Tests if a string is alphabetic'
    test_input = True
    while test_input is True:
        user_input = input(prompt)
        invalid_input = [x for x in user_input.replace("-","").replace(" ","") if not x.isalpha()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        else:
            return user_input.title()

def getalnum(prompt):
    'Tests if a string is alphanumeric'
    test_input = True
    while test_input is True:
        user_input = input(prompt)
        invalid_input = [x for x in user_input.replace("-","").replace(" ","") if not x.isalnum()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        else:
            return user_input.title()

def getnumeric(prompt):
    'Tests if a string is numeric'
    test_input = True
    while test_input is True:
        user_input = input(prompt)
        invalid_input = [x for x in user_input if not x.isnumeric()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        else:
            return user_input

# CLASSES
class Person:
    'A person includes a first name, last name, street address, zip code, and phone number.'
    def __init__(self):
        self.setfirstname()
        self.setlastname()
        self.setaddress()
        self.setzipcode()
        self.setphonenumber()

    def setfirstname(self):
        'Prompts user to enter a first name'
        self.firstname = getalpha("Enter first name: ")

    def setlastname(self):
        'Prompts user to enter a last name'
        self.lastname = getalpha("Enter last name: ")

    def setaddress(self):
        'Prompts user to enter a street address'
        self.address = getalnum("Enter street address: ")

    def setzipcode(self):
        'Prompts user to enter a zipcode'
        test_input = True
        while test_input is True:
            user_input = getnumeric("Enter zipcode: ")
            if len(user_input) != 5:
                print("Please try again. That is not a valid zipcode.")
            else:
                test_input = False
                self.zipcode = user_input

    def setphonenumber(self):
        'Prompts user to enter a phone number'
        test_input = True
        while test_input is True:
            user_input = getnumeric("Enter phone number without dashes: ")
            if len(user_input) != 10:
                print("Please try again. That is not a valid phone number.")
            else:
                test_input = False
                self.phonenumber = user_input[:3] + "-" + user_input[3:6] + "-" + user_input[6:]

    def display(self):
        'Displays all of a Persons information'
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Zipcode: {self.zipcode}")
        print(f"Phonenumber: {self.phonenumber}")
