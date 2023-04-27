#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
Student descends from Person. In addition to the fields available 
in Person, a Student contains a major field of study and a grade 
point average as well as methods that override the Person methods 
to accept and display these additional facts.
'''

from Person import Person

class Student(Person):
    'Adds a major and GPA to a Person'
    def __init__(self, F='', L='', A='', Z='', P='', M='', G=''):
        super().__init__(F, L, A, Z, P)
        self.major = M
        self.gpa = G

    def display(self):
        super().display()
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")
