#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=inconsistent-return-statements
'''
A Person contains a first name, last name, street address, zip code, and phone number. 
The class also includes a method that sets each data field, using a series of dialog boxes and 
a display method that displays all of a Persons information on a single line at the command line on the screen.
'''

### FUNCTIONS ###
def getalpha(prompt):
    'Tests if a string is alphabetic'
    test_input = True
    while test_input is True:
        user_input = input(prompt) # prompt parameter allows reusability of this function
        invalid_input = [x for x in user_input.replace("-","").replace(" ","") if not x.isalpha()] # Tests every char thats not a space or dash
        if len(invalid_input) > 0: # Anything that didn't pass is automatically put into a list, and we check if that was given data
            print(f"Please try again. Invalid input found: {invalid_input}") #displays the list of invalid characters
        elif user_input == "": # if no input entered
            print("Please try again. No input given.")
        else:
            return user_input.title() # if everything passes, returns the input with capitalization

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

def getfirstname():
    'Prompts user to enter a first name'
    firstname = getalpha("Enter first name: ")
    return firstname

def getlastname():
    'Prompts user to enter a last name'
    lastname = getalpha("Enter last name: ")
    return lastname

def getaddress():
    'Prompts user to enter a street address'
    address = getalnum("Enter street address: ")
    return address

def getzipcode():
    'Prompts user to enter a zipcode'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter zipcode: ")
        if len(user_input) != 5:
            print("Please try again. That is not a valid zipcode.")
        else:
            test_input = False
            zipcode = user_input
    return zipcode

def getphonenumber():
    'Prompts user to enter a phone number'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter phone number without dashes: ")
        if len(user_input) != 10:
            print("Please try again. That is not a valid phone number.")
        else:
            test_input = False
            phonenumber = user_input[:3] + "-" + user_input[3:6] + "-" + user_input[6:] # returns input with dashes in appropriate place
    return phonenumber

### CLASS ###
class Person:
    'A person includes a first name, last name, street address, zip code, and phone number.'
    def __init__(self, firstname=None, lastname=None, address=None, zipcode=None, phonenumber=None): # Setting a default value makes the arguments optional
        self.firstname = firstname if firstname is not None else getfirstname() # If no value is given, it automatically runs the above functions to obtain the value
        self.lastname = lastname if lastname is not None else getlastname() # This setup allows data to be given to the class through any other methods
        self.address = address if address is not None else getaddress() # Or by user input if the data was not taken from another source
        self.zipcode = zipcode if zipcode is not None else getzipcode()
        self.phonenumber = phonenumber if phonenumber is not None else getphonenumber()

    def setfirstname(self):
        "Sets a firstname manually"
        self.firstname = getfirstname()

    def setlastname(self):
        "Sets a lastname manually"
        self.lastname = getlastname()

    def setaddress(self):
        "Sets a street address manually"
        self.address = getaddress()

    def setzipcode(self):
        "Sets a zipcode manually"
        self.zipcode = getzipcode()

    def setphonenumber(self):
        "Sets a phone number manually"
        self.phonenumber = getphonenumber()

    def display(self):
        'Displays all of a Persons information'
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Zipcode: {self.zipcode}")
        print(f"Phonenumber: {self.phonenumber}")
