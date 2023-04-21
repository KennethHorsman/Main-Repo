#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=pointless-string-statement
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
            print("Please enter information for at least 1 person.")
        else:
            gettype = False
            for i, employee in enumerate(c_list):
                print(f"\n- College Employee #{i+1} -")
                employee.display()
            for i, faculty_member in enumerate(f_list):
                print(f"\n- Faculty Member #{i+1} -")
                faculty_member.display()
            for i, student in enumerate(s_list):
                print(f"\n- Student #{i+1} -")
                student.display()

"All the below code is just something I was messing around with, it's not required for the project. I don't know how to make it more compact or efficient."

person_dict = {
    "C" : "college employee",
    "F" : "faculty member",
    "S" : "student"
}

info_dict = {
    "F" : 'setfirstname',
    "L" : 'setlastname',
    "A" : 'setaddress',
    "Z" : 'setzipcode',
    "P" : 'setphonenumber',
    "N" : 'setssn',
    "D" : 'setdepartment',
    "T" : 'settenuredstatus',
    "M" : 'setmajor',
    "G" : 'setgpa'
}

prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
getinput = True
while getinput is True:
    if prompt_edit == "Y":
        persontype = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()
        if persontype in ("C","F","S"):
            number = input(f"Enter which {person_dict[persontype]} you would like to edit: ")
            if number.isdigit():
                if persontype == "C":
                    if int(number) in range(1,len(c_list)+1):
                        c_info = input("Enter 'F' to edit first name, 'L' for last name, 'A' for address, 'Z' for zipcode, 'P' for phonenumber, 'N' for SSN, 'S' for salary, or 'D' for department: ").upper()
                        if c_info in info_dict:
                            c_item = info_dict[c_info]
                            if callable(getattr(c_list[int(number)-1], c_item)):
                                getattr(c_list[int(number)-1], c_item)()
                                print(f"\nCollege employee #{number} has been updated to the following:")
                                c_list[int(number)-1].display()
                            else:
                                print("Error: This change cannot be made.") # This code should never be accesed but I'll put it here anyways
                        else:
                            print("Error: Please only enter one of the below options.")
                    else:
                        print("Sorry, there is no college employee with that number.")
                if persontype == "F":
                    if int(number) in range(1,len(f_list)+1):
                        f_info = input("Enter 'F' to edit first name, 'L' for last name, 'A' for address, 'Z' for zipcode, 'P' for phonenumber, 'N' for SSN, 'S' for salary, 'D' for department, or 'T' for tenured status: ").upper()
                        if f_info in info_dict:
                            f_item = info_dict[f_info]
                            if callable(getattr(f_list[int(number)-1], f_item)):
                                getattr(f_list[int(number)-1], f_item)()
                                print(f"\nFaculty member #{number} has been updated to the following:")
                                f_list[int(number)-1].display()
                            else:
                                print("Error: This change cannot be made.")
                        else:
                            print("Error: Please only enter one of the below options.")
                    else:
                        print("Sorry, there is no faculty member with that number.")
                if persontype == "S":
                    if int(number) in range(1,len(s_list)+1):
                        s_info = input("Enter 'F' to edit first name, 'L' for last name, 'A' for address, 'Z' for zipcode, 'P' for phonenumber, 'M' for major, or 'G' for GPA: ").upper()
                        if s_info in info_dict:
                            s_item = info_dict[s_info]
                            if callable(getattr(s_list[int(number)-1], s_item)):
                                getattr(s_list[int(number)-1], s_item)()
                                print(f"\nStudent #{number} has been updated to the following:")
                                s_list[int(number)-1].display()
                            else:
                                print("Error: This change cannot be made.")
                        else:
                            print("Error: Please only enter one of the below options.")
                    else:
                        print("Sorry, there is no student with that number.")
            else:
                print("Error: That is not a valid number.")
        prompt_edit = input("Would you still like to edit any of the information entered? (y/n): ").upper()
    elif prompt_edit == "N":
        print("All lists created successfully.")
        getinput = False
    else:
        print("Error: Please only enter one of the below options.")
