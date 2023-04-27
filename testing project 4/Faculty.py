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
    def __init__(self, F='', L='', A='', Z='', P='', N='', S='', D='', T=None):
        super().__init__(F, L, A, Z, P, N, S, D)
        self.tenured = T

    def display(self):
        super().display()
        print(f"Tenured: {self.tenured}")
