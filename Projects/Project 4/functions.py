def get_edit():
    getting_input = True
    while getting_input:
        prompt_edit = input("Would you like to edit any of the information entered? Enter 'Y' for yes or 'N' for no: ")
        if prompt_edit == 'Y':
            return True
        elif prompt_edit == 'N':
            return False
        else:
            print("Please try again. That is not a valid option.")

# if ask_to_edit is True:
#     make it loop the ask_to_edit function

def get_person_type():
    getting_input = True
    while getting_input:
        person_type = input("Enter 'C' for college employee, 'F' for faculty member, or 'S' for student: ").upper()
        if person_type in ("C","F","S"):
            list_to_use = person_dict[person_type][3]
            phrase_to_use = person_dict[person_type][1]
            if len(list_to_use) == 0:
                print(f"Please try again. There is no {phrase_to_use} to edit.")
            else:
                return person_type
        else:
            print("Please try again. That is not a valid option.")

def get_person_number(person_type):
    list_to_use = person_dict[person_type][3]
    phrase_to_use = person_dict[person_type][1]
    
    person_number = input(f"Enter which {phrase_to_use} you would like to edit: ")
    if person_number.isdigit():
        if int(person_number) in range(1,len(list_to_use)+1):
            return int(person_number)
        else:
            print(f"Please try again. There is no {phrase_to_use} with that number.")
    else:
        print("Please try again. That is not a valid number.")

def get_edit_key(person_type):
    list_to_use = person_dict[person_type][3]
    phrase_to_use = person_dict[person_type][1]

    print("- List of Keys -")
    for key, value in key_dict.items():
        print(f"'{key}' for {value[1]}")
    getting_input = True
    while getting_input:
        edit_key = input("Enter one of the above keys: ").upper()
        if edit_key in ['F','L','A','Z','P'] or edit_key in person_dict[person_type][2]:
            return edit_key
        else:
            if edit_key in key_dict:
                print(f"Please try again. That is not a valid key for a {phrase_to_use}.")
            else:
                print("Please try again. That is not a valid key.")

def edit_and_display(person_type, edit_key):
    list_to_use = person_dict[person_type][3]
    phrase_to_use = person_dict[person_type][1]
    method_call = key_dict[edit_key][0]

    getattr(list_to_use[person_number-1], method_call)()
    print(f"\n{phrase_to_use.capitalize()} #{person_number} has been updated to the following:")
    list_to_use[person_number-1].display()
    print()

# Have this inside main, with a flag to check if user ever agreed to edit
def finish_up():
    if not get_edit():
        for key, value in person_dict.items():
        display_list_objects(value[3], value[1].title())
        
    college_employees = len(person_dict["C"][3]) 
    faculty_members = len(person_dict["F"][3])
    students = len(person_dict["S"][3])
    print(f"List created successfully. There {'are' if college_employees != 1 else 'is'} " # F strings used to display each number of persons created, with proper grammar
            f"{college_employees} college employee{'s' if college_employees != 1 else ''}, "
            f"{faculty_members} faculty member{'s' if faculty_members != 1 else ''}, "
            f"and {students} student{'s' if students != 1 else ''}.")
        
    
    