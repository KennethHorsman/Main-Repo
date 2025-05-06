##### Made By Kenneth Horsman (30260797)

import os
import re

desc = """A program that removes or duplicates characters from a string of text is a simple tool relevant to cryptography. 
While only a character replacement ability is considered a substituion cipher, these processes work in a similar way. All of 
these methods can be used as simple obfuscation of text, making it harder to interpret. However, it could fairly easily 
be broken by studying the pattern of which characters appear to have been modified. Lastly, character removal or
duplication also be used to compress or add padding to the data so it fits a specific block size."""

def main(): #calling all the functions
    getting_choice = True
    original_string = ""

    while getting_choice:
        option = input("\nYou may choose from the following options: \n" 
        "1) Take a string from a .txt file \n" 
        "2) Manually input a string \n"
        "3) View more information about this tool \n"
        "4) Exit tool\n"
        "Enter choice: ")

        match option:
            case "1":
                original_string = get_string_file()
            case "2":
                original_string = get_string_manual()
            case "3":
                print_description()
            case "4":
                return # Not sure if this is the right thing to do
            case _:
                print("Invalid input. Please select option 1 - 4.")

        if original_string:
            working_string = original_string
            status = "edit"

            while status == "edit":
                modification_type = get_modification_type()
                if modification_type:
                    characters = get_characters(modification_type)
                    call_func = eval(f"{modification_type}_text")
                    new_string = call_func(working_string, characters)
                    print_results(new_string, original_string)
                    status = get_status()

                    working_string = new_string
                else:
                    status = ""

            while status == "save":
                save_type = get_save_type()
                file_name = get_save_file()
                if file_name:
                    status = save_string(file_name, new_string, save_type)


def get_string_file():
    getting_file = True

    while getting_file:
        file_name = input("Enter the name of the .txt file (or type EXIT to return to menu): ").strip().upper()
        if file_name == "EXIT":
            return None
        else:
            if ".TXT" not in file_name:
                file_name += ".TXT"

            working_string = check_errors(file_name, "file")
            if working_string:
                return working_string


def get_string_manual():
    getting_string = True

    while getting_string:
        working_string = input("Enter the string of text you would like to modify: ")
        if check_errors(working_string, "manual"):
            return working_string


def get_modification_type():
    getting_input = True

    while getting_input:
        modification_type = input("\nYou may choose from following options: \n" 
        "1) Remove characters \n" 
        "2) Duplicate characters \n" 
        "3) Return to tool menu\n"
        "Enter choice: ")

        match modification_type:
            case "1":
                return "remove"
            case "2":
                return "duplicate"
            case "3":
                return None
            case _:
                print("Invalid input. Please select option 1 - 3.")


def get_characters(modification_type):
    characters = []
    character_input = input(f"Enter all the characters (case-sensitive) you would like to {modification_type}, with no separation: ")

    for x in character_input:
        characters.append(x)
    return characters


def get_status():
    option = input("Please select one of the following options: \n" 
    "1) Make changes to the new string \n" 
    "2) Save the new string to a file\n"
    "3) Return to tool menu\n"
    "Enter choice: ")

    match option:
        case "1":
            return "edit"
        case "2":
            return "save"
        case "3":
            return None
        case _:
            print("Invalid input. Please select option 1 - 3.")
            return get_status()


def duplicate_text(working_string, characters):
    new_string = working_string

    for x in characters:
        new_string = new_string.replace(x, x * 2)
    return new_string


def remove_text(working_string, characters):
    new_string = working_string

    for x in characters:
        new_string = new_string.replace(x, '')
    return new_string


def check_errors(input_data, source_type):
    if source_type == "manual":
        return validate_string(input_data, source_type)
    else:
        try:
            with open(f"{input_data}", "r") as file:
                working_string = file.read()
                return validate_string(working_string.strip(), source_type)                
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None


def validate_string(working_string, source_type):
    if not working_string:
        print("No string found. Please try again.")
        return
    elif len(working_string) > 1000:
        print("The given string is too long. Please try again.")
        return
    else:
        if source_type == "file":
            print(f"You have selected the following string: {working_string}")
        return working_string
        

def get_save_type():
    getting_option = True

    while getting_option:
        modification_type = input("\nYou may choose from following options: \n" 
        "1) Create a new file \n" 
        "2) Append to an existing file \n" 
        "3) Overwrite an existing file\n"
        "4) Return to tool menu\n"
        "Enter choice: ")

        match modification_type:
            case "1":
                return "x"
            case "2":
                return "a"
            case "3":
                return "w"
            case "4":
                return None
            case _:
                print("Invalid input. Please select option 1 - 4.")


def get_save_file():
    getting_file = True

    while getting_file:
        file_name = input("Please enter the name of the .txt file (or type EXIT to return to menu): ").strip()
        
        if file_name == "EXIT" or not file_name:
            return None
        elif re.search(r'[<>:"/\\|?*]', file_name):
            print("You have entered an invalid file name. Please try again.")
            return None
        else:
            if ".txt" not in file_name:
                file_name += ".txt"
            return file_name


def save_string(file_name, new_string, save_type):
        try:
            if save_type in "wa" and not os.path.exists(file_name):
                raise FileNotFoundError

            with open(f"{file_name}", f"{save_type}") as file:
                file.write(new_string)

            success = "Success"
            if save_type == "x":
                success += "fully created "
            elif save_type == "a":
                success += "fully appended to "
            else:
                success += "full overwrite of "
            success += file_name + "."

            print(success)
            # print(f"Success{"fully created a" if save_type == "x"
            #                  else "fully appended to" if save_type == "a"
            #                  else "ful overwrite of"} {file_name}.")
            return None
            
        except FileNotFoundError:
            print("File does not exist. Please try again.")
        except FileExistsError:
            print("File already exists. Please try again.")
        except PermissionError:
            print("No permission to write to file. Please try again.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

        return "save"


def print_description():
    # with open("rem_or_dup_desc.txt", "r") as file:
    print(desc)
    print("You are now being returned to the tool menu.")
    return None


def print_results(new_string, original_string):
    print(f"\nYour original string was: {original_string}")

    if new_string == original_string:
        print("You have not made any modifications to this string.\n")
    else:
        print(f"\nYour modified string is: {new_string}\n")

def remove_or_duplicate_menu():
    print("This program allows you to remove and duplicate characters from an alphanumeric string of text.")
    main()


if __name__=="__main__":
    print("This program allows you to remove and duplicate characters from an alphanumeric string of text.")
    main()