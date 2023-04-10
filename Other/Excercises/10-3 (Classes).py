#pylint: disable=missing-class-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=trailing-whitespace
#pylint: disable=invalid-name

'''
Design a class named TermPaper that holds an author's name, 
the subject of the paper, and an assigned letter grade. 
Include methods to set the values for each data field and 
display the values for each data field. Create the class diagram and 
write the pseudocode that defines the class.

------------------------------
|         TermPaper          |
------------------------------
| - authorName: String       |
| - subject: String          |
| - letterGrade: String      |
------------------------------
| + setAuthorName(name: String) : void |
| + setSubject(subject: String) : void |
| + setLetterGrade(grade: String) : void |
| + getAuthorName() : String |
| + getSubject() : String |
| + getLetterGrade() : String |
| + __str__() : String |
------------------------------

CLASS TermPaper:
    FUNCTION init(self):
        SET author to empty string
        SET subject to empty string
        SET grade to empty string

    FUNCTION set_author_name(self, name):
        SET author to name

    FUNCTION set_subject(self, subject):
        SET subject to subject

    FUNCTION set_grade(self, grade):
        SET grade to grade

    FUNCTION get_author_name(self):
        RETURN author

    FUNCTION get_subject(self):
        RETURN subject

    FUNCTION get_grade(self):
        RETURN grade
'''

class TermPaper:
    def __init__(self, author=None, subject=None, grade=None):
        self.author = author
        self.subject = subject
        self.grade = grade
        
    def set_author(self, author):
        self.author = author
        
    def set_subject(self, subject):
        self.subject = subject
        
    def set_grade(self, grade):
        self.grade = grade
        
    def display(self):
        for field, value in self.__dict__.items():
            if value is not None:
                print(f"{field.title()}: {value}")
        
        
paper = TermPaper()
paper.set_author("Jane Smith")
paper.set_subject("History of the American Revolution")
paper.set_grade("A")
paper.display()
