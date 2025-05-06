def main(): #calling all the functions
    option = input("\nYou may choose from the following options: \n" 
    "1) Take a string from a .txt file \n" 
    "2) Manually input a string \n"
    "3) View more information about this program \n"
    "4) Exit program\n\n"
    "Enter choice: ")

    match option:
        case "1":
            original_string = get_string_file()
        case "2":
            original_string = get_string_manual()
        case "3":
            print_description()
        case "4":
            print("Exiting program.")
            exit()
        case _:
            print("Invalid input. Please select option 1 - 3.")

    given_string = original_string
    editing_string = True

    while editing_string:
        modification_type = get_modification_type()
        characters = get_characters(modification_type)
        call_func = eval(f"{modification_type}_text")
        new_string = call_func(given_string, characters)
        print_results(new_string, original_string)
        editing_string = ask_for_edit()
        given_string = new_string


def duplicate_text(given_string, characters):
    new_string = given_string

    for x in characters:
        new_string = new_string.replace(x, x * 2)

    return new_string


def remove_text(given_string, characters):
    new_string = given_string

    for x in characters:
        new_string = new_string.replace(x, '')

    return new_string


def get_string_manual():
    given_string = input("Enter the string of text you would like to modify: ")

    return given_string


def get_string_file():
    getting_file = True

    while getting_file:
        file_name = input("Enter the name of the .txt file (or type EXIT to return to menu): ").strip().upper()

        if file_name == "EXIT":
            main()

        else:
            if ".txt" not in file_name:
                file_name += ".txt"

            try:
                with open(f"{file_name}", "r") as file:
                    given_string = file.readline()
            except:
                print("File not found. Please try again.")

    return given_string


def get_characters(modification_type):
    characters = []
    character_input = input(f"Enter all the characters (case-sensitive) you would like to {modification_type}, with no separation: ")

    for x in character_input:
        characters.append(x)

    return characters


def ask_for_edit():
    option = input("Please select one of the following options: \n" 
    "1) Make more changes to the current string \n" 
    "2) Modify a new string \n" 
    "3) Exit program\n\n" \
    "Enter choice: ")

    match option:
        case "1":
            return True
        case "2":
            main()
        case "3":
            print("Exiting program.")
            exit()
        case _:
            print("Invalid input. Please select option 1 - 3.")


def print_description():
    print("This program...\n")
    
    option = input("You may choose from following options: \n" 
    "1) Return to main menu \n" 
    "2) Exit Program\n\n" \
    "Enter choice: ")

    match option:
        case "1":
            main()
        case "2":
            print("Exiting program.")
            exit()
        case _:
            print("Invalid input. Please select option 1 - 3.")


def get_modification_type():
    getting_input = True

    while getting_input:
        modification_type = input("\nYou may choose from following options: \n" 
        "1) Remove characters \n" 
        "2) Duplicate characters \n" 
        "3) Return to main menu\n\n"
        "Enter choice: ")
    
        match modification_type:
            case "1":
                return "remove"
            case "2":
                return "duplicate"
            case "3":
                main()
            case _:
                print("Invalid input. Please select option 1 - 3.")


def print_results(new_string, given_string):
    print(f"Your original string was: {given_string}")
    print(f"Your modified string is: {new_string}\n")


if __name__=="__main__":
    print("This program allows you to remove and duplicate characters within a string of text.")
    main()