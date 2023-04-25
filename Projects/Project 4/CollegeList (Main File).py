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

from CollegeEmployee import CollegeEmployee
from Faculty import Faculty
from Student import Student

# Helper Function
def display_list_objects(list_objects, object_type):
    'Displays the attributes of an object'
    if list_objects:
        for i, obj in enumerate(list_objects):
            print(f"\n- {object_type} #{i+1} -")
            obj.display()
        print()

# Declarations
person_dict = {
    # Key : method call, phrase to use, applicable keys, max number of persons, list of objects
    "C" : [CollegeEmployee, "college employee", ["N","S","D"], [], 4],
    "F" : [Faculty, "faculty member", ["N","S","D","T"], [], 3],
    "S" : [Student, "student", ["M","G"], [], 7,]
}

key_dict = {
    # Key : method call, phrase to use
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

# Main Program - Creates list of persons based off user input
print("This program creates and displays a list of up to 4 college employees, 3 faculty members, and 7 students in the U.S.")

get_person = True
while get_person is True:
    person_key = input("Enter 'C' for college employee, 'F' for faculty, 'S' for student, or 'Q' to quit: ").upper()

    if person_key not in ("C","F","S","Q"):
        print("Please try again. Invalid key entered.")

    elif person_key != "Q":
        max_persons = person_dict[person_key][4]
        person_list = person_dict[person_key][3]
        if len(person_list) < max_persons:
            method_call = person_dict[person_key][0]
            person_list.append(method_call())
        else:
            phrase_to_use = person_dict[person_key][1]
            print(f"Maxium number of {phrase_to_use}s reached.")

    else:
        if sum(len(value[1]) for value in person_dict.values()) == 0:
            print("Please enter information for at least one person.")
        else:
            get_person = False
            for key, value in person_dict.items():
                display_list_objects(value[3], value[1].title())

# Allows the user to edit any of the info they've previously entered
prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()

ask_to_display = False
getinput = True
while getinput is True:

    if prompt_edit == "Y":
        ask_to_display = True
        repeatoption_personkey = True

        while repeatoption_personkey is True:
            person_key = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()

            if person_key in ("C","F","S"):
                person_list = person_dict[person_key][3]
                phrase_to_use = person_dict[person_key][1]

                if len(person_list) == 0:
                    print(f"Please try again. There is no {phrase_to_use} to edit.")
                else:
                    repeatoption_personkey = False
                    repeatoption_number = True

                    while repeatoption_number is True:
                        number = input(f"Enter which {phrase_to_use} you would like to edit: ")

                        if number.isdigit():
                            if int(number) in range(1,len(person_list)+1):
                                print("- List of keys -")
                                for key, value in key_dict.items():
                                    print(f"'{key}' for {value[1]}")

                                repeatoption_number = False
                                repeatoption_infokey = True

                                while repeatoption_infokey is True:
                                    info_key = input("Enter one of the above keys: ").upper()

                                    if info_key in ['F','L','A','Z','P'] or info_key in person_dict[person_key][2]:
                                        repeatoption_infokey = False
                                        method_call = key_dict[info_key][0]
                                        getattr(person_list[int(number)-1], method_call)()
                                        print(f"\n{phrase_to_use.capitalize()} #{number} has been updated to the following:")
                                        person_list[int(number)-1].display()
                                        print()
                                    else:
                                        if info_key in key_dict:
                                            print(f"Please try again. That is not a valid key for a {phrase_to_use}.")
                                        else:
                                            print("Please try again. That is not a valid key.")

                            else:
                                print(f"Please try again. There is no {phrase_to_use} with that number.")

                        else:
                            print("Please try again. That is not a valid number.")

            else:
                print("Please try again. That is not a valid key.")

        prompt_edit = input("Would you still like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()

    elif prompt_edit == "N":
        getinput = False

        while ask_to_display is True:
            display_again = input("Would you like to display the revised list of persons? Enter 'Y' for yes or 'N' for no: ").upper()
            if display_again == "Y":
                ask_to_display = False
                for key, value in person_dict.items():
                    display_list_objects(value[3], value[1].title())
            elif display_again == "N":
                ask_to_display = False
            else:
                print("Please try again. That is not a valid option.")

        college_employees = len(person_dict["C"][3])
        faculty_members = len(person_dict["F"][3])
        students = len(person_dict["S"][3])
        print(f"List created successfully. There {'are' if college_employees != 1 else 'is'} "
              f"{college_employees} college employee{'s' if college_employees != 1 else ''}, "
              f"{faculty_members} faculty member{'s' if faculty_members != 1 else ''}, "
              f"and {students} student{'s' if students != 1 else ''}.")

    else:
        print("Please try again. That is not a valid option.")
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
