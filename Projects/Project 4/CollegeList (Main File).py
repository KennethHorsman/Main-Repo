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

# Helper Functions
def display_list_objects(list_objects, object_type):
    '''Displays the attributes of an object.
    
    list_objects = specified list of objects to loop through
    object_type = title of the list of objects
    '''
    if list_objects:
        for index, obj in enumerate(list_objects): # Enumerate loops through the list of objects with {index, object} pairs
            print(f"\n- {object_type} #{index+1} -") # Displays the title of object with an incrementing index for each object
            obj.display() # Calls the display method for each object it loops through
        print() # Prints an empty line as a separator


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
    person_key = input("Enter 'C' for college employee, 'F' for faculty, 'S' for student, or 'Q' to quit: ").upper() #Automatically converts input to upper to prevent errors

    if person_key not in ("C","F","S","Q"):
        print("Please try again. Invalid key entered.")

    elif person_key != "Q":
        max_persons = person_dict[person_key][4] # finds the max number of the user's chosen person type by accessing the dictionary with the given key
        person_list = person_dict[person_key][3] # Finds which persons list to append to by accessing the dictionary with the given key
        if len(person_list) < max_persons: # Checks to see if the number of persons in the accessed list is less than the max number of the user's chosen
            method_call = person_dict[person_key][0] # Finds the name of the method that will be used to create the person object by accessing the dictionary with the given key
            person_list.append(method_call()) # Calls the method, and once the object is created, appends it to the corresponding list of persons
        else: # If the number of persons in the accessed list is equal to the max number of persons for that list...
            phrase_to_use = person_dict[person_key][1] # Finds the correct phrase to use by accessing the dictionary with the given key
            print(f"Maxium number of {phrase_to_use}s reached.")

    else:
        if sum(len(value[3]) for value in person_dict.values()) == 0: # Loops through each of the lists in the dictionary and sums together the length (number of persons)
            print("Please enter information for at least one person.")
        else:
            get_person = False
            for key, value in person_dict.items(): # Items returns (key,value) pairs of a dictionary, all of which are looped through here
                display_list_objects(value[3], value[1].title()) # Calls the display function for each object appended to each list, setting 'phrase to use' as the title


# Allows the user to edit any of the info they've previously entered
prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()

ask_to_display = False
getinput = True
while getinput is True:

    if prompt_edit == "Y":
        ask_to_display = True # Only if the user chooses to edit the information entered, they will recieve a prompt at the end to display the revised information
        repeatoption_personkey = True # I set separate flags for each input in order to allow individual questions to be repeated if invalid input is given

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

                        if number.isdigit(): # Checks to see if the user entered a whole number
                            if int(number) in range(1,len(person_list)+1): # Checks to see if the number is within the range of the applicable list of persons
                                repeatoption_number = False
                                repeatoption_infokey = True
                                print("- List of keys -")
                                for key, value in key_dict.items():
                                    print(f"'{key}' for {value[1]}") # Displays the key and its 'phrase to use'

                                while repeatoption_infokey is True:
                                    info_key = input("Enter one of the above keys: ").upper()

                                    if info_key in ['F','L','A','Z','P'] or info_key in person_dict[person_key][2]: # Checks if user entered a default key or one specific to the person type
                                        repeatoption_infokey = False
                                        method_call = key_dict[info_key][0]
                                        getattr(person_list[int(number)-1], method_call)() #Finds the value of the specific object, what method to call on it, and then calls the method
                                        print(f"\n{phrase_to_use.capitalize()} #{number} has been updated to the following:") # Capitalize calls .upper() on the first letter only
                                        person_list[int(number)-1].display() # Calls the display method for that specific object
                                        print()
                                    else:
                                        if info_key in key_dict: # If the key given is in the dictionary but not applicable to that person type...
                                            print(f"Please try again. That is not a valid key for a {phrase_to_use}.")
                                        else: # If the key given is not in the dictionary at all...
                                            print("Please try again. That is not a valid key.")

                            else: # If the number given when asked for which person to edit is not within the range of the list of objects for that person type...
                                print(f"Please try again. There is no {phrase_to_use} with that number.")

                        else: # If the number given when asked for which person to edit is not a whole number...
                            print("Please try again. That is not a valid number.")

            else: # If the user did not enter 'C' or 'F' or 'S' when prompted to choose which person type to edit...
                print("Please try again. That is not a valid key.")

        # Once the edit has been completed, the user can choose to make more edits or quit
        prompt_edit = input("Would you still like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()

    elif prompt_edit == "N":
        getinput = False

        # If the user made an edit...
        while ask_to_display is True:
            display_again = input("Would you like to display the revised list of persons? Enter 'Y' for yes or 'N' for no: ").upper()

            if display_again == "Y":
                ask_to_display = False
                for key, value in person_dict.items():
                    display_list_objects(value[3], value[1].title()) # Repeating the same thing after the user entered 'Q' in the beginning

            elif display_again == "N":
                ask_to_display = False

            # If the user did not enter 'Y' or 'N' when prompted to display the revsied list...
            else:
                print("Please try again. That is not a valid option.")

        college_employees = len(person_dict["C"][3]) # Now it's calculating the number of each person type by getting the length of each list of objects in the dictionary
        faculty_members = len(person_dict["F"][3])
        students = len(person_dict["S"][3])
        print(f"List created successfully. There {'are' if college_employees != 1 else 'is'} " # F strings used to display each number of persons created with proper grammar
              f"{college_employees} college employee{'s' if college_employees != 1 else ''}, "
              f"{faculty_members} faculty member{'s' if faculty_members != 1 else ''}, "
              f"and {students} student{'s' if students != 1 else ''}.")

    # If user did not enter 'Y' or 'N' when prompted to edit...
    else:
        print("Please try again. That is not a valid option.")
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ").upper()
