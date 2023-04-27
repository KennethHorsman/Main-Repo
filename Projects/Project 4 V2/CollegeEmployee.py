#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
CollegeEmployee descends from Person. 
A CollegeEmployee also includes a Social Security number, an annual salary, 
and a department name, as well as methods that override the Person methods 
to accept and display all CollegeEmployee data.
'''

from Person import Person, getalpha, getnumeric

def getssn():
    'Prompts user to enter an SSN'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter SSN without dashes: ")
        if len(user_input) != 9:
            print("Please try again. That is not a valid SSN.")
        else:
            test_input = False
            ssn = user_input[:3] + "-" + user_input[3:5] + "-" + user_input[5:]
    return ssn

def getsalary():
    'Prompts user to enter an annual salary'
    user_input = getnumeric("Enter salary with no symbols: ")
    salary = f"${int(user_input):,}"
    return salary

def getdepartment():
    'Prompts user to enter a department'
    department = getalpha("Enter department: ")
    return department

### CLASSES ###
class CollegeEmployee(Person):
    'Adds an SSN, salary, and department to a Person'
    def __init__(self, ssn=None, salary=None, department=None):
        super().__init__()
        self.ssn = ssn
        self.salary = salary
        self.department = department

    def setssn(self,ssn):
        'Sets an ssn manually'
        self.ssn = ssn

    def setsalary(self, salary):
        'Sets a salary manually'
        self.salary = salary

    def setdepartment(self, department):
        'Sets a department manually'
        self.department = department

    def display(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
