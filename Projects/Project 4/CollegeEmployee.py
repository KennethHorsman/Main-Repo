#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
CollegeEmployee descends from Person. 
A CollegeEmployee also includes a Social Security number, an annual salary, 
and a department name, as well as methods that override the Person methods 
to accept and display all CollegeEmployee data.
'''

from Person import Person

def is_valid_number(number):
    'Determines if a number is a valid number'
    try:
        float(number)
        return True
    except ValueError:
        return False

class CollegeEmployee(Person):
    'Adds an SSN, salary, and department to a Person'
    def __init__(self):
        super().__init__()
        self.setssn()
        self.setsalary()
        self.setdepartment()

    def setssn(self):
        'Prompts user to enter a social security number'
        getssn = True
        while getssn is True:
            ssn_input = input("Enter social security number: ")
            invalid_input = [x for x in ssn_input.replace("-","") if not x.isnumeric()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif ssn_input == "":
                print("Error: No input given.")
            elif len(ssn_input) != 9 and len(ssn_input) != 11:
                print("That is not a valid SSN.")
            elif len(ssn_input) == 11:
                testdigits = ssn_input[:3] + ssn_input[4:6] + ssn_input[7:]
                testdashes = ssn_input[3] + ssn_input[6]
                if testdigits.isdigit() and testdashes == "--":
                    self.ssn = ssn_input
                    getssn = False
                else:
                    print("That is not a valid SSN.")
            else:
                ssn_with_dashes = ssn_input[:3] + "-" + ssn_input[3:5] + "-" + ssn_input[5:]
                self.ssn = ssn_with_dashes
                getssn = False

    def setsalary(self):
        'Prompts user to enter an annual salary'
        getsalary = True
        while getsalary is True:
            salary_input = input("Enter annual salary: ").replace("$","").replace(",","")
            invalid_input = [x for x in salary_input.replace(".","") if not x.isnumeric()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif salary_input == "":
                print("Error: No input given.")
            elif not is_valid_number(salary_input):
                print("That is not a valid number.")
            else:
                self.salary = f"${float(salary_input):,.2f}"
                getsalary = False

    def setdepartment(self):
        'Prompts user to enter a department'
        getdepartment = True
        while getdepartment is True:
            department_input = input("Enter department: ")
            invalid_input = [x for x in department_input.replace("-","").replace(" ","") if not x.isalpha()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif department_input == "":
                print("Error: No input given.")
            else:
                self.department = department_input.title()
                getdepartment = False

    def display(self):
        super().display()
        print(f"Social Security Number: {self.ssn}")
        print(f"Annual salary: {self.salary}")
        print(f"Department: {self.department}")
