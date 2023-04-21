#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
Faculty descends from CollegeEmployee. This class also includes a 
Boolean field that indicates whether the Faculty member is tenured, 
as well as methods that override the CollegeEmployee methods to accept 
and display this additional piece of information.
'''

from CollegeEmployee import CollegeEmployee

class Faculty(CollegeEmployee):
    'Adds tenured status to a college employee.'
    def __init__(self):
        super().__init__()
        self.settenuredstatus()

    def settenuredstatus(self):
        'Prompts user to enter whether the Faculty member is tenured.'
        getstatus = True
        while getstatus is True:
            tenured_input = input("If tenured, enter 'Y'. Otherwise, enter 'N': ").upper()
            if tenured_input == "":
                print("Error: No input given.")
            elif tenured_input != "Y" and tenured_input != "N":
                print("Error: Please only enter 'Y' or 'N'.")
            elif tenured_input == "Y":
                self.tenured = True
                getstatus = False
            else:
                self.tenured = False
                getstatus = False

    def display(self):
        super().display()
        print(f"Tenured: {self.tenured}")
        print('')