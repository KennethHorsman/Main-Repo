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
                print(f"- College Employee #{i+1} -")
                employee.display()
            for i, faculty_member in enumerate(f_list):
                print(f"- Faculty Member #{i+1} -")
                faculty_member.display()
            for i, student in enumerate(s_list):
                print(f"- Student #{i+1} -")
                student.display()

person_dict = {
    "C" : ["college employee", c_list, ["N","S","D"]],
    "F" : ["faculty member", f_list, ["N","S","D","T"]],
    "S" : ["student", s_list, ["M","G"]]
}

info_dict = {
    "F" : ['setfirstname', 'first name'],
    "L" : ['setlastname', 'last name'],
    "A" : ['setaddress', 'address'],
    "Z" : ['setzipcode', 'zipcode'],
    "P" : ['setphonenumber', 'phone number'],
    "N" : ['setssn', 'SSN'],
    "S" : ["setsalary", 'salary'],
    "D" : ['setdepartment', 'department'],
    "T" : ['settenuredstatus', 'tenured status'],
    "M" : ['setmajor', 'major',],
    "G" : ['setgpa', 'GPA']
}

prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
getinput = True
while getinput is True:
    if prompt_edit == "Y":
        persontype = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()
        if persontype in ("C","F","S"):
            person_list = person_dict[persontype][1]
            if len(person_list) == 0:
                print(f"Sorry, there is no {person_dict[persontype][0]} to edit.")
            else:
                number = input(f"Enter which {person_dict[persontype][0]} you would like to edit: ")
                if number.isdigit():
                    if int(number) in range(1,len(person_list)+1):
                        print("- List of keys -")
                        for key, value in info_dict.items():
                            print(f"'{key}' for {value[1]}")
                        repeatoption = True
                        while repeatoption is True:
                            info_key = input("Enter one of the above keys: ").upper()
                            if info_key in ['F','L','A','Z','P'] or info_key in person_dict[persontype][2]:
                                repeatoption = False
                                method_call = info_dict[info_key][0]
                                getattr(person_list[int(number)-1], method_call)()
                                print(f"{person_dict[persontype][0].capitalize()} #{number} has been updated to the following:")
                                person_list[int(number)-1].display()
                            else:
                                print("Error: That is not a valid key.")
                    else:
                        print("Sorry, there is no college employee with that number.")
                else:
                    print("Error: That is not a valid number.")
        else:
            print("Error: That is not a valid key.")
        prompt_edit = input("Would you still like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
    elif prompt_edit == "N":
        print("All lists created successfully.")
        getinput = False
    else:
        print("Error: That is not a valid option.")
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
