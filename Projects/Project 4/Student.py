'''
Student descends from Person. In addition to the fields available 
in Person, a Student contains a major field of study and a grade 
point average as well as methods that override the Person methods 
to accept and display these additional facts.
'''

from Person import Person

class Student(Person):
    'Adds a major and GPA to a Person'
    def __init__(self):
        super().__init__()
        self.setmajor()
        self.setgpa()

    def setmajor(self):
        'Prompts user to enter a major'
        getmajor = True
        while getmajor is True:
            major_input = input("Enter major: ")
            invalid_input = [x for x in major_input.replace("-","").replace(" ","") if not x.isalpha()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif major_input == "":
                print("Error: No input given.")
            else:
                self.major = major_input.title()
                getmajor = False

    def setgpa(self):
        'Prompts user to enter a GPA'
        getgpa = True
        while getgpa is True:
            gpa_input = input("Enter GPA on a 4.0 scale: ")
            invalid_input = [x for x in gpa_input.replace(".","") if not x.isnumeric()]
            if len(invalid_input) > 0:
                print(f"Invalid input found: {invalid_input}")
            elif gpa_input == "":
                print("Error: No input given.")
            elif len(gpa_input) == 3:
                if gpa_input[1] == "." and gpa_input[0].isdigit() and gpa_input[2].isdigit():
                    self.gpa = gpa_input
                    getgpa = False
                else:
                    print("That is not a valid GPA.")
            else:
                print("That is not a valid GPA.")

    def display(self):
        super().display()
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")
