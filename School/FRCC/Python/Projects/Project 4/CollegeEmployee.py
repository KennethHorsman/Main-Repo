#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
CollegeEmployee descends from Person. 
A CollegeEmployee also includes a Social Security number, an annual salary, 
and a department name, as well as methods that override the Person methods 
to accept and display all CollegeEmployee data.
'''

from Person import Person, getalpha, getnumeric # Imports the necessary class and functions from Person.py

### FUNCTIONS ###
def getssn():
    'Prompts user to enter an SSN'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter SSN without dashes: ") # If I allow dashes, I have to check they are ONLY in the correct places, and  have two possible return values
        if len(user_input) != 9: # An SSN without dashes is 9 digits long
            print("Please try again. That is not a valid SSN.")
        else:
            test_input = False
            ssn = user_input[:3] + "-" + user_input[3:5] + "-" + user_input[5:] # Adds dashes in the appropriate places
    return ssn

def getsalary():
    'Prompts user to enter an annual salary'
    user_input = getnumeric("Enter salary with no symbols: ")
    salary = f"${int(user_input):,}" # Formats the number to add a dollar sign and a comma as a thousands separtor
    return salary

def getdepartment():
    'Prompts user to enter a department'
    department = getalpha("Enter department: ")
    return department

### CLASSES ###
class CollegeEmployee(Person):
    'Adds an SSN, salary, and department to a Person'
    def __init__(self, ssn=None, salary=None, department=None): 
        super().__init__() # Initalizes the Person class and inherits all of its properties
        self.ssn = ssn if ssn is not None else getssn() 
        self.salary = salary if salary is not None else getsalary() 
        self.department = department if department is not None else getdepartment()

    def setssn(self):
        'Sets an ssn manually'
        self.ssn = getssn() # If I call this method, it will run the appropriate function to change to ssn value

    def setsalary(self):
        'Sets a salary manually'
        self.salary = getsalary()

    def setdepartment(self):
        'Sets a department manually'
        self.department = getdepartment()

    def display(self):
        super().display() # Calls Person's display method
        print(f"Social Security Number: {self.ssn}") # I am printing these separately so I can customize the title
        print(f"Annual salary: {self.salary}")
        print(f"Department: {self.department}")
