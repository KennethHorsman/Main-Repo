'''
A Person contains a first name, last name, street address, zip code, and phone number. 
The class also includes a method that sets each data field, using a series of dialog boxes and 
a display method that displays all of a Persons information on a single line at the command line on the screen.
'''

class Person:
    def __init__(self):
        self.setfirstname()
        self.setlastname()
        self.setaddress()
        self.setzipcode()
        self.setphonenumber()
        
    def setfirstname(self):
        getfirstname = True
        while getfirstname is True:
            firstname_input = input("Enter first name: ")
            invalid_input = [x for x in firstname_input.replace("-","").replace(" ","") if not x.isalpha()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif firstname_input == "":
                print("Error: No input given.")
            else:
                self.firstname = firstname_input.title()
                getfirstname = False
                
    def setlastname(self):
        getlastname = True
        while getlastname is True:
            lastname_input = input("Enter last name: ")
            invalid_input = [x for x in lastname_input.replace("-","").replace(" ","") if not x.isalpha()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif lastname_input == "":
                print("Error: No input given.")
            else:
                self.lastname = lastname_input.title()
                getlastname = False

    def setaddress(self):
        getaddress = True
        while getaddress is True:
            address_input = input("Enter address: ")
            invalid_input = [x for x in address_input.replace("-","").replace(" ","") if not x.isalnum()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif address_input == "":
                print("Error: No input given.")
            else:
                self.address = address_input.title()
                getaddress = False
                
    def setzipcode(self):
        getzipcode = True
        while getzipcode is True:
            zipcode_input = input("Enter zipcode: ")
            invalid_input = [x for x in zipcode_input.replace("-","").replace(" ","") if not x.isnumeric()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif zipcode_input == "":
                print("Error: No input given.")
            elif len(zipcode_input.replace(" ","")) != 5:
                print("That is not a valid zipcode.") 
            else:
                self.zipcode = zipcode_input
                getzipcode = False
                
    def setphonenumber(self):
        getphonenumber = True
        while getphonenumber is True:
            phonenumber_input = input("Enter phone number: ")
            invalid_input = [x for x in phonenumber_input.replace("-","") if not x.isnumeric()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif phonenumber_input == "":
                print("Error: No input given.")
            elif len(phonenumber_input) != 10 and len(phonenumber_input) != 12:
                print("That is not a valid phone number.") 
            elif len(phonenumber_input) == 12:
                testdigits = phonenumber_input[:3] + phonenumber_input[4:7] + phonenumber_input[9:]
                testdashes = phonenumber_input[3] + phonenumber_input[7]
                if testdigits.isdigit() and testdashes == "--":
                    self.phonenumber = phonenumber_input
                    getphonenumber = False
                else:
                    print("That is not a valid phone number.")
            else:
                phonenumber_with_dashes = phonenumber_input[:3] + "-" + phonenumber_input[3:6] + "-" + phonenumber_input[6:]
                self.phonenumber = phonenumber_with_dashes
                getphonenumber = False
        
    def display(self):
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Zipcode: {self.zipcode}")
        print(f"Phonenumber: {self.phonenumber}")
