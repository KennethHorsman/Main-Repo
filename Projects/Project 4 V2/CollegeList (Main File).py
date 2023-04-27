#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=inconsistent-return-statements
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

def main():
    'Allows user to create and edit a list of persons, which will then be displayed.'
    prompting_creation = True
    prompting_edit = True
    edits_made = False

    print("This program allows the user to create and edit a list of 4 college employees, 3 faculty members, and 7 students.")

    while prompting_creation:
        selection = get_person_or_quit()
        if selection != "Q":
            if validate_person_type(selection):
                create_person(selection)
        else:
            prompting_creation = False

    display_all_persons()

    while prompting_edit:
        if get_edit():
            edits_made = True
            person_type = get_person_type()
            person_number = get_person_number(person_type)
            edit_key = get_edit_key(person_type)
            edit_and_display(person_type, person_number, edit_key)
        else:
            prompting_edit = False

    finish_up(edits_made)


### MAIN FUNCTIONS ###
def get_person_or_quit():
    'Asks user to enter which type of person they would like to add to the list, or quit'
    getting_input = True

    while getting_input:
        person_type = input("Enter 'C' for college employee, 'F' for faculty,"
                            " 'S' for student, or 'Q' to quit: ").upper()

        if person_type not in ("C","F","S","Q"):
            print("Please try again. That is not a valid option.")
        elif person_type == "Q" and sum(len(value[PERSON_LIST_INDEX]) for value in person_dict.values()) == 0:
            print("Please enter information for at least one person.")
        else:
            return person_type


def validate_person_type(person_type):
    'Determines if the person type selected is usable'
    max_persons = person_dict[person_type][MAX_PERSONS_INDEX]
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]

    if len(list_to_use) == max_persons:
        print(f"Please try again. Maximum number of {phrase_to_use}s reached.")
        return False
    return True


def create_person(person_type):
    'Allows user to create a new person of the specified type.'
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    method_call = person_dict[person_type][METHOD_INDEX]
    applicable_keys = person_dict[person_type][KEY_INDEX]
    arguments_to_use = []
    arguments_value = []

    for key in DEFAULT_KEYS:
        arguments_to_use.append(key)
    for key in applicable_keys:
        arguments_to_use.append(key)

    for key in arguments_to_use:
        function_call = key_dict[key][METHOD_INDEX]
        arguments_value.append(function_call())

    list_to_use.append(method_call(*arguments_value))

def display_all_persons():
    'Displays all persons created.'

    print("List of Persons:")
    for value in person_dict.values():
        display_list_objects(value[PERSON_LIST_INDEX], value[PHRASE_INDEX].title())
    print()


def display_list_objects(list_objects, object_type):
    'Displays the attributes of an object.'

    if list_objects:
        for index, obj in enumerate(list_objects): # Enumerate loops through the list of objects with {index, object} pairs
            print(f"\n- {object_type} #{index+1} -") # Displays the title of object with an incrementing index for each object
            obj.display() # Calls the display method for each object it loops through


### EDITING FUNCTIONS ###
def get_edit():
    'Asks user if they want to edit any information in the list of persons.'
    getting_input = True

    while getting_input:
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()

        if prompt_edit == 'Y':
            return True
        if prompt_edit == 'N':
            return False

        print("Please try again. That is not a valid option.")


def get_person_type():
    'Asks user which person type they want to edit.'
    getting_input = True

    while getting_input:
        person_type = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()

        if person_type in ("C","F","S"):
            list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
            phrase_to_use = person_dict[person_type][PHRASE_INDEX]
            if len(list_to_use) == 0:
                print(f"Please try again. There is no {phrase_to_use} to edit.")
            else:
                return person_type

        else:
            print("Please try again. That is not a valid option.")


def get_person_number(person_type):
    'Asks user the number of the person they want to edit.'
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]
    getting_input = True

    while getting_input:
        person_number = input(f"Enter which {phrase_to_use} you would like to edit: ")
        if person_number.isdigit():
            if int(person_number) in range(1,len(list_to_use)+1):
                return int(person_number)
            print(f"Please try again. There is no {phrase_to_use} with that number.")
        else:
            print("Please try again. That is not a valid number.")


def get_edit_key(person_type):
    'Asks user which information they want to edit.'
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]
    getting_input = True

    print("- List of Keys -")
    for key, value in key_dict.items():
        print(f"'{key}' for {value[PHRASE_INDEX]}")

    while getting_input:
        edit_key = input("Enter one of the above keys: ").upper()
        if edit_key in DEFAULT_KEYS or edit_key in person_dict[person_type][KEY_INDEX]:
            return edit_key
        if edit_key in key_dict:
            print(f"Please try again. That is not a valid key for a {phrase_to_use}.")
        else:
            print("Please try again. That is not a valid key.")


def edit_and_display(person_type, person_number, edit_key):
    "Allows user to make the edit, then displays the updated information for that specific person."
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]
    method_call = key_dict[edit_key][METHOD_INDEX]

    getattr(list_to_use[person_number-1], str(method_call))()
    print(f"\n{phrase_to_use.capitalize()} #{person_number} has been updated to the following:")
    list_to_use[person_number-1].display()
    print()


def finish_up(edits_made):
    'Displays the revised list of persons if edits were made, and displays the total number of each person type created.'
    college_employees = len(person_dict["C"][PERSON_LIST_INDEX])
    faculty_members = len(person_dict["F"][PERSON_LIST_INDEX])
    students = len(person_dict["S"][PERSON_LIST_INDEX])

    print(f"\nList created successfully. There {'are' if college_employees != 1 else 'is'} "
            f"{college_employees} college employee{'s' if college_employees != 1 else ''}, "
            f"{faculty_members} faculty member{'s' if faculty_members != 1 else ''}, "
            f"and {students} student{'s' if students != 1 else ''}.")

    if edits_made:
        print("Revised List of Persons:")
        for value in person_dict.values():
            display_list_objects(value[PERSON_LIST_INDEX], value[PHRASE_INDEX].title())

### INFORMATION FUNCTIONS ###
def getalpha(prompt):
    'Tests if a string is alphabetic'
    test_input = True
    while test_input is True:
        user_input = input(prompt)
        invalid_input = [x for x in user_input.replace("-","").replace(" ","") if not x.isalpha()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        else:
            return user_input.title()

def getalnum(prompt):
    'Tests if a string is alphanumeric'
    test_input = True
    while test_input is True:
        user_input = input(prompt)
        invalid_input = [x for x in user_input.replace("-","").replace(" ","") if not x.isalnum()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        else:
            return user_input.title()

def getnumeric(prompt):
    'Tests if a string is numeric'
    test_input = True
    while test_input is True:
        user_input = input(prompt)
        invalid_input = [x for x in user_input if not x.isnumeric()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        else:
            return user_input

def setfirstname():
    'Prompts user to enter a first name'
    firstname = getalpha("Enter first name: ")
    return firstname

def setlastname():
    'Prompts user to enter a last name'
    lastname = getalpha("Enter last name: ")
    return lastname

def setaddress():
    'Prompts user to enter a street address'
    address = getalnum("Enter street address: ")
    return address

def setzipcode():
    'Prompts user to enter a zipcode'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter zipcode: ")
        if len(user_input) != 5:
            print("Please try again. That is not a valid zipcode.")
        else:
            test_input = False
            zipcode = user_input
    return zipcode

def setphonenumber():
    'Prompts user to enter a phone number'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter phone number without dashes: ")
        if len(user_input) != 10:
            print("Please try again. That is not a valid phone number.")
        else:
            test_input = False
            phonenumber = user_input[:3] + "-" + user_input[3:6] + "-" + user_input[6:]
    return phonenumber

def setmajor():
    'Prompts user to enter a major'
    major = getalpha("Enter major: ")
    return major

def setgpa():
    'Prompts user to enter a GPA'
    test_input = True
    while test_input is True:
        user_input = input("Enter GPA on a 4.0 scale: ")
        invalid_input = [x for x in user_input.replace(".","") if not x.isnumeric()]
        if len(invalid_input) > 0:
            print(f"Please try again. Invalid input found: {invalid_input}")
        elif user_input == "":
            print("Please try again. No input given.")
        elif not len(user_input) == 3 or not (0.0 <= float(user_input) <= 4.0) or not ((user_input[0] and user_input[2]).isnumeric() and user_input[1] == "."):
            print("Please try again. That is not a valid GPA.")
        else:
            test_input = False
            gpa = user_input
    return gpa

def setssn():
    'Prompts user to enter an SSN'
    test_input = True
    while test_input is True:
        user_input = getnumeric("Enter SSN without dashes: ")
        if len(user_input) != 9:
            print("Please try again. That is not a valid SSN.")
        else:
            test_input = False
            ssn = user_input[:3] + "-" + user_input[3:5] + "-" + user_input[5:]
    return ssn

def setsalary():
    'Prompts user to enter an annual salary'
    user_input = getnumeric("Enter salary with no symbols: ")
    salary = f"${int(user_input):,}"
    return salary

def setdepartment():
    'Prompts user to enter a department'
    department = getalpha("Enter department: ")
    return department

def settenuredstatus():
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

### DECLARATIONS###
person_dict = {
    # Key : method call, phrase to use, applicable keys, list of objects, max number of persons
    "C" : [CollegeEmployee, "college employee", ["N","S","D"], [], 4],
    "F" : [Faculty, "faculty member", ["N","S","D","T"], [], 3],
    "S" : [Student, "student", ["M","G"], [], 7,]
}

key_dict = {
    # Key : method call, phrase to use
    "F" : [setfirstname, 'first name'],
    "L" : [setlastname, 'last name'],
    "A" : [setaddress, 'address'],
    "Z" : [setzipcode, 'zipcode'],
    "P" : [setphonenumber, 'phone number'],
    "N" : [setssn, 'SSN'],
    "S" : [setsalary, 'salary'],
    "D" : [setdepartment, 'department'],
    "T" : [settenuredstatus, 'tenured status'],
    "M" : [setmajor, 'major',],
    "G" : [setgpa, 'GPA']
}

DEFAULT_KEYS = ["F","L","A","Z","P"]
METHOD_INDEX = 0
PHRASE_INDEX = 1
KEY_INDEX = 2
PERSON_LIST_INDEX = 3
MAX_PERSONS_INDEX = 4



if __name__=="__main__":
    main()
