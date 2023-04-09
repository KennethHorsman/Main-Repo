'''
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
        SET author_name to empty string
        SET subject to empty string
        SET grade to empty string

    FUNCTION set_author_name(self, name):
        SET author_name to name

    FUNCTION set_subject(self, subject):
        SET subject to subject

    FUNCTION set_grade(self, grade):
        SET grade to grade

    FUNCTION get_author_name(self):
        RETURN author_name

    FUNCTION get_subject(self):
        RETURN subject

    FUNCTION get_grade(self):
        RETURN grade
'''

class TermPaper:
    
    def __init__(self):
        self.authorName = ""
        self.subject = ""
        self.letterGrade = ""

    def setAuthorName(self, authorName):
        self.authorName = authorName

    def setSubject(self, subject):
        self.subject = subject

    def setLetterGrade(self, letterGrade):
        self.letterGrade = letterGrade

    def getAuthorName(self):
        return self.authorName

    def getSubject(self):
        return self.subject

    def getLetterGrade(self):
        return self.letterGrade

    def __str__(self):
        return "Author Name: " + self.authorName + "\nSubject: " + self.subject + "\nLetter Grade: " + self.letterGrade
    
myTermPaper = TermPaper()
myTermPaper.setAuthorName("John Smith")
myTermPaper.setSubject("History of Art")
myTermPaper.setLetterGrade("A+")
print(myTermPaper)
