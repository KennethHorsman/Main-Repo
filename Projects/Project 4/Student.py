#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
Student descends from Person. In addition to the fields available 
in Person, a Student contains a major field of study and a grade 
point average as well as methods that override the Person methods 
to accept and display these additional facts.
'''

from Person import Person, getalpha

class Student(Person):
    'Adds a major and GPA to a Person'
    def __init__(self):
        super().__init__()
        self.setmajor()
        self.setgpa()

    def setmajor(self):
        'Prompts user to enter a major'
        self.major = getalpha("Enter major: ")

    def setgpa(self):
        'Prompts user to enter a GPA'
        test_input = True
        while test_input is True:
            user_input = input("Enter GPA on a 4.0 scale: ")
            invalid_input = [x for x in user_input.replace(".","") if not x.isnumeric()]
            if len(invalid_input) > 0:
                print(f"Please try again. Invalid input found: {invalid_input}")
            elif user_input == "":
                print("Please try again. No input given.")
            elif not len(user_input) == 3 or not ((user_input[0] and user_input[2]).isnumeric() and user_input[1] == "."):
                print("Please try again. That is not a valid GPA.")
            else:
                test_input = False
                self.gpa = user_input

    def display(self):
        super().display()
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")
