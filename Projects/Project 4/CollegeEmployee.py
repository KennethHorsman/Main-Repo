#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
CollegeEmployee descends from Person. 
A CollegeEmployee also includes a Social Security number, an annual salary, 
and a department name, as well as methods that override the Person methods 
to accept and display all CollegeEmployee data.
'''

from Person import Person, getalpha, getnumeric

class CollegeEmployee(Person):
    'Adds an SSN, salary, and department to a Person'
    def __init__(self):
        super().__init__()
        self.setssn()
        self.setsalary()
        self.setdepartment()

    def setssn(self):
        'Prompts user to enter an SSN'
        test_input = True
        while test_input is True:
            user_input = getnumeric("Enter SSN without dashes: ")
            if len(user_input) != 9:
                print("Please try again. That is not a valid phone number.")
            else:
                test_input = False
                self.ssn = user_input[:3] + "-" + user_input[3:5] + "-" + user_input[5:]

    def setsalary(self):
        'Prompts user to enter an annual salary'
        user_input = getnumeric("Enter salary without any symbols: ")
        self.salary = f"${float(user_input):,.2f}"

    def setdepartment(self):
        'Prompts user to enter a department'
        self.department = getalpha("Enter department: ")

    def display(self):
        super().display()
        print(f"Social Security Number: {self.ssn}")
        print(f"Annual salary: {self.salary}")
        print(f"Department: {self.department}")
