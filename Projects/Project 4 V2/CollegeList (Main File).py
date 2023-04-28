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

def main(): # Using a main function allows me to display my code top down
    'Allows user to create and edit a list of persons, which will then be displayed.'
    prompting_creation = True
    prompting_edit = True
    edits_made = False

    print("This program allows the user to create and edit a list of 4 college employees, 3 faculty members, and 7 students.")

    while prompting_creation: # This flag allows user to keep creating persons until they enter Q
        selection = get_person_or_quit()

        if selection != "Q":
            if validate_person_type(selection): # Function determines whether the person limit has been reached for their selection
                create_person(selection) # If not (above func return true / valid), creates person using the type they selected

        else:
            prompting_creation = False

    display_all_persons() # Once they choose to quit creating persons, this function displays them all at once

    while prompting_edit: # This flag allows edits to be made until the user enters 'N'
        if get_edit(): # Returns a boolean indicating whether they choose to edit or not
            edits_made = True # This flag is used to tell the finish_up function whether or not the user made edits
            person_type = get_person_type() # Same as get_person_or_quit() but without Q
            person_number = get_person_number(person_type) # Identifies the specific person to edit
            edit_key = get_edit_key(person_type) # Identifies the attribute they want to edit

            edit_and_display(person_type, person_number, edit_key) # Uses all the above variables as parameters to make the edit & display result

        else:
            prompting_edit = False

    finish_up(edits_made) # Totals the final number of persons and displays a final, revised list only if edits_made is true

#################
### FUNCTIONS ###
#################
def get_person_or_quit():
    'Asks user to enter which type of person they would like to add to the list, or quit'
    getting_input = True

    while getting_input:
        person_type = input("Enter 'C' for college employee, 'F' for faculty,"
                            " 'S' for student, or 'Q' to quit: ").upper() # .upper() prevents an error if they enter a lowercase

        if person_type not in ("C","F","S","Q"):
            print("Please try again. That is not a valid option.")

        elif person_type == "Q" and sum(len(value[PERSON_LIST_INDEX]) for value in person_dict.values()) == 0: # If no persons created and they try to quit...
            print("Please enter information for at least one person.")

        else:
            return person_type


def validate_person_type(person_type):
    'Determines if the person type selected is usable'
    max_persons = person_dict[person_type][MAX_PERSONS_INDEX] # Identifies the dict, the key, and the value, to be used as a variable
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]

    if len(list_to_use) == max_persons: # If the list that the persons are appended to has reached its respective max number...
        print(f"Please try again. Maximum number of {phrase_to_use}s reached.") # Having a phrase for each person type allows custom messages
        return False

    return True # I don't need a second if statement because the above statement has a return


def create_person(person_type):
    'Allows user to create a new person of the specified type.'
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    method_call = person_dict[person_type][METHOD_INDEX]

    list_to_use.append(method_call()) # Since the classes are imported, they're callable. Once the object is created, it's appended to the respective list


def display_all_persons():
    'Displays all persons created.'

    print("List of Persons:")
    for value in person_dict.values(): # Loops through the value of each key in the dictionary
        display_list_objects(value[PERSON_LIST_INDEX], value[PHRASE_INDEX].title()) # Uses display func with parameters as specific values from the dict
    print() # Simply prints a blank line for aesthetic purposes


def display_list_objects(list_objects, object_title):
    'Displays the attributes of an object.'

    if list_objects: # If the specified list has anything in it...
        for index, obj in enumerate(list_objects): # Enumerate loops through the list of objects with {index, object} pairs
            print(f"\n- {object_title} #{index+1} -") # Displays the provided title of each object with an incrementing index for each object
            obj.display() # Calls the display method - from its class - for each object it loops through


def get_edit():
    'Asks user if they want to edit any information in the list of persons.'
    getting_input = True

    while getting_input:
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()

        if prompt_edit == 'Y':
            return True # Since the function is automatically returning a value, there's no need to set getting_input to False
        if prompt_edit == 'N':
            return False

        print("Please try again. That is not a valid option.") # If the input is not 'y' or 'n', this is automatically accessed


def get_person_type():
    'Asks user which person type they want to edit.'
    getting_input = True

    while getting_input:
        person_type = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()

        if person_type in ("C","F","S"):
            list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
            phrase_to_use = person_dict[person_type][PHRASE_INDEX]

            if len(list_to_use) == 0: # Checks if the selected person type was ever created
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

        if person_number.isdigit(): # Checks if the number they entered was a whole, positive number

            if int(person_number) in range(1,len(list_to_use)+1): # Converts it to an int to check if it's in the range of the length of that person type's list
                return int(person_number) # If it is, returns it as an integer so it doesn't have to be converted anywhere else

            print(f"Please try again. There is no {phrase_to_use} with that number.")

        else:
            print("Please try again. That is not a valid number.")


def get_edit_key(person_type):
    'Asks user which information they want to edit.'
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]
    getting_input = True

    print("- List of Keys -")
    for key, value in key_dict.items(): # Loops through every (key, value) pair in the dictionary
        print(f"'{key}' for {value[PHRASE_INDEX]}") # Displays it using the specific value (since the values are lists)

    while getting_input:
        edit_key = input("Enter one of the above keys: ").upper()

        if edit_key in DEFAULT_KEYS or edit_key in person_dict[person_type][KEY_INDEX]: # Checks if input is a person's attribute or one specific to that person type
            return edit_key

        if edit_key in key_dict: # If it's in the dictionary, but not specific to the person type...
            print(f"Please try again. That is not a valid key for a {phrase_to_use}.")

        else:
            print("Please try again. That is not a valid key.")


def edit_and_display(person_type, person_number, edit_key):
    "Allows user to make the edit, then displays the updated information for that specific person."
    list_to_use = person_dict[person_type][PERSON_LIST_INDEX]
    phrase_to_use = person_dict[person_type][PHRASE_INDEX]
    method_call = key_dict[edit_key][METHOD_INDEX]
    specific_object = list_to_use[person_number-1] # Once the correct list is identified, it uses the given number to access the specific object

    getattr(specific_object, method_call)() # Essentially accesses the value of the object, what method to call on it (as str) then calls it with () outside
    print(f"\n{phrase_to_use.capitalize()} #{person_number} has been updated to the following:") # Capitalize applies .upper to the first letter only
    specific_object.display()
    print()


def finish_up(edits_made):
    'Displays the revised list of persons if edits were made, and displays the total number of each person type created.'
    college_employees = len(person_dict["C"][PERSON_LIST_INDEX]) # Counts the len of the list of objects within the values for that specific key
    faculty_members = len(person_dict["F"][PERSON_LIST_INDEX])
    students = len(person_dict["S"][PERSON_LIST_INDEX])

    if edits_made: # Only if the parameter is true...
        print("Revised List of Persons:")
        for value in person_dict.values(): # Same as what happens in the display_all function
            display_list_objects(value[PERSON_LIST_INDEX], value[PHRASE_INDEX].title())

    print(f"\nList created successfully. There {'are' if college_employees != 1 else 'is'} " # This just allows a statement to not be on one long line
            f"{college_employees} college employee{'s' if college_employees != 1 else ''}, " # f-strings with if-statements allow proper grammar based on variables
            f"{faculty_members} faculty member{'s' if faculty_members != 1 else ''}, "
            f"and {students} student{'s' if students != 1 else ''}.")

####################
### DECLARATIONS ###
####################
person_dict = {
    # Key : method call, phrase to use, applicable keys, list of objects, max number of persons
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

DEFAULT_KEYS = ["F","L","A","Z","P"] # These are the attributes of the person class
METHOD_INDEX = 0 # The method used to create a person or edit a specific sttribute
PHRASE_INDEX = 1 # Phrase to use for custom messages depending on person type (key)
KEY_INDEX = 2 # Each persont type has their own additional set of keys applicable specifically to them
PERSON_LIST_INDEX = 3 # The list of objects each person is appended to
MAX_PERSONS_INDEX = 4 # The maximum number of persons for that type


if __name__=="__main__": # Instead of calling all the functions in the main program, requiring them to be pre-defined, I use this and only call main()
    main()
