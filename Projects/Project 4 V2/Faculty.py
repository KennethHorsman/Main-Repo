#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
Faculty descends from CollegeEmployee. This class also includes a 
Boolean field that indicates whether the Faculty member is tenured, 
as well as methods that override the CollegeEmployee methods to accept 
and display this additional piece of information.
'''

from CollegeEmployee import CollegeEmployee

### FUNCTIONS ###
def gettenuredstatus():
    'Prompts user to enter whether the Faculty member is tenured.'
    test_input = True
    while test_input is True:
        tenured_input = input("If tenured, enter 'Y'. Otherwise, enter 'N': ").upper()
        if tenured_input == "":
            print("Please try again. No input given.")
        elif tenured_input != "Y" and tenured_input != "N":
            print("Please try again. That is not a valid option.")
        elif tenured_input == "Y":
            return True
        else:
            return False

### CLASSES ###
class Faculty(CollegeEmployee):
    'Adds tenured status to a college employee.'
    def __init__(self, tenured=None):
        super().__init__()
        self.tenured = tenured if tenured is not None else gettenuredstatus()

    def settenuredstatus(self, tenured):
        'Sets a tenured status manually'
        self.tenured = tenured

    def display(self):
        super().display()
        print(f"Tenured: {self.tenured}")
