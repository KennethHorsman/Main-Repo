#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=inconsistent-return-statements
'''
A Person contains a first name, last name, street address, zip code, and phone number. 
The class also includes a method that sets each data field, using a series of dialog boxes and 
a display method that displays all of a Persons information on a single line at the command line on the screen.
'''

class Person:
    'A person includes a first name, last name, street address, zip code, and phone number.'
    def __init__(self, F='', L='', A='', Z='', P=''):
        self.firstname = F
        self.lastname = L
        self.address = A
        self.zipcode = Z
        self.phonenumber = P

    def display(self):
        'Displays all of a Persons information'
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Zipcode: {self.zipcode}")
        print(f"Phonenumber: {self.phonenumber}")
