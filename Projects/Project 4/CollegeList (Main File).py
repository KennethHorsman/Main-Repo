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

def display_list_objects(list_objects, object_type):
    'Displays the attributes of an object'
    if list_objects:
        for i, obj in enumerate(list_objects):
            print(f"\n- {object_type} #{i+1} -")
            obj.display()
        print()

c_list = []
f_list = []
s_list = []

person_dict = {
    # Key : Phrase to use, list of objects, applicable keys, method call, max number of objects
    "C" : ["college employee", c_list, ["N","S","D"], CollegeEmployee, 4],
    "F" : ["faculty member", f_list, ["N","S","D","T"], Faculty, 3],
    "S" : ["student", s_list, ["M","G"], Student, 7]
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

print("This program creates and displays a list of up to 4 college employees, 3 faculty members, and 7 students.")
get_person = True
while get_person is True:
    person_key = input("Enter 'C' for college employee, 'F' for faculty, 'S' for student, or 'Q' to quit: ").upper()
    if person_key not in ("C","F","S","Q"):
        print("Please try again. Invalid key entered.")
    elif person_key != "Q":
        max_persons = person_dict[person_key][4]
        person_list = person_dict[person_key][1]
        if len(person_list) < max_persons:
            method_call = person_dict[person_key][3]
            person_list.append(method_call())
        else:
            phrase_to_use = person_dict[person_key][0]
            print(f"Maxium number of {phrase_to_use}s reached.")
    else:
        if len(c_list) + len(f_list) + len(s_list) == 0:
            print("Please enter information for at least one person.")
        else:
            get_person = False
            for key, value in person_dict.items():
                display_list_objects(value[1], value[0].title())

prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
getinput = True
while getinput is True:
    if prompt_edit == "Y":
        repeatoption_personkey = True
        while repeatoption_personkey is True:
            person_key = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()
            if person_key in ("C","F","S"):
                person_list = person_dict[person_key][1]
                phrase_to_use = person_dict[person_key][0]
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
                                            print(f"Please try again. That is not a valid key for a {person_dict[person_key][0]}.")
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
        print("List created successfully.")
        getinput = False
    else:
        print("Please try again. That is not a valid option.")
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
