#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
CollegeEmployee descends from Person. 
A CollegeEmployee also includes a Social Security number, an annual salary, 
and a department name, as well as methods that override the Person methods 
to accept and display all CollegeEmployee data.
'''

from Person import Person

class CollegeEmployee(Person):
    'Adds an SSN, salary, and department to a Person'
    def __init__(self, F='', L='', A='', Z='', P='', N='', S='', D=''):
        super().__init__(F, L, A, Z, P)
        self.ssn = N
        self.salary = S
        self.department = D

    def display(self):
        super().display()
        print(f"Social Security Number: {self.ssn}")
        print(f"Annual salary: {self.salary}")
        print(f"Department: {self.department}")
