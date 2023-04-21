#pylint: disable=line-too-long
#pylint: disable=invalid-name
'''
Write an application named CollegeList that implements a list 
of four “regular” CollegeEmployee, three Faculty, and seven Students. 

1. Prompt the user to specify which type of persons data will be entered (C, F, or S), 
or allow the user to quit (Q). While the user chooses to continue (that is, does not quit), 
accept data entry for the appropriate type of Person. 

2. If the user attempts to enter data for more than four CollegeEmployees, 
three Faculty, or seven Students, display an error message. 

3. When the user quits, display a report on the screen listing each group of Persons 
under the appropriate heading of “College Employees,” “Faculty,” or “Students.” 

4. If the user has not entered data for one or more types of Persons during a session, 
display an appropriate message under the appropriate heading.
'''

from Faculty import Faculty
from Student import Student
from CollegeEmployee import CollegeEmployee

print("This program creates and displays a list of up to 4 college employees, 3 faculty members, and 7 students.")

c_list = []
f_list = []
s_list = []

gettype = True
while gettype is True:
    type_input = input("Enter 'C' for college employee, 'F' for faculty, 'S' for student, or 'Q' to quit: ").upper()
    if type_input not in ("C","F","S","Q"):
        print("Error: Invalid input.")
    elif type_input =="C":
        if len(c_list) < 4:
            c_list.append(CollegeEmployee())
        else:
            print("Maximum number of college employee's reached.")
    elif type_input =="F":
        if len(f_list) < 3:
            f_list.append(Faculty())
        else:
            print("Maximum number of faculty members reached.")
    elif type_input =="S":
        if len(s_list) < 7:
            s_list.append(Student())
        else:
            print("Maximum number of students reached.")
    else:
        if len(c_list) + len(f_list) + len(s_list) == 0:
            print("Please enter at least 1 person.")
        else:
            gettype = False
            for x in range(len(c_list)):
                print(f"\n- College Employee #{x+1} -")
                c_list[x].display()
            for x in range(len(f_list)):
                print(f"\n- Faculty Member #{x+1} -")
                f_list[x].display()
            for x in range(len(s_list)):
                print(f"\n- Student #{x+1} -")
                s_list[x].display()
