# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=inconsistent-return-statements
'''
3. Create the logic for a program that accepts a user's birth month and year and 
passes them to a method that calculates the user's age in the current month and 
returns the value to the main program to be be displayed.
'''

from datetime import datetime

def main():
    'Displays the users current age'
    age = calculate_age()
    month_as_string = month_dict[currentMonth]
    day_suffix = get_suffix()
    print(f'The current date is {month_as_string.title()} {currentDay}{day_suffix}, {currentYear}.')
    print(f"You are {age} year{'s' if age > 1 else ''} old.")

def calculate_age():
    'Calculates the users age'
    user_day, user_month, user_year = validate_user_date()
    year_diff = currentYear - user_year
    precedes_flag = (currentMonth, currentDay) < (user_month, user_day)
    age = year_diff - precedes_flag
    return age

def validate_user_date():
    'Determines if birth day is a valid date'
    year = get_user_year()
    leap_year = determine_leap_year(year)
    if leap_year:
        month_end_dict[2] = month_end_dict.get(2)+1
    month = get_user_month()
    get_day = True
    while get_day is True:
        day = get_user_day()
        if day == 0 or day > month_end_dict[month]:
            print("Error: That is an invalid date for your month of birth.")
        else:
            get_day = False
    return day, month, year

def get_user_year():
    'Prompts user for their birth year'
    get_year = True
    while get_year is True:
        year_input = input("Please enter the year you were born: ")
        if year_input.isnumeric() and float(year_input).is_integer() and 1000 <= float(year_input) <= currentYear: # In case they wanna determine the age of a historical figure or something lol
            get_year = False # useless code but good to visualize
            return int(year_input)
        print("Error: Invalid Character(s) Detected.")

def determine_leap_year(year):
    'Determines if birth year was a leap year'
    leap_year = False
    if year % 100:
        if year % 400:
            leap_year = True
    if not year % 100:
        if year % 4:
            leap_year = True
    return leap_year

def get_user_month():
    'Prompts user for their birth month'
    get_month = True
    while get_month is True:
        month_input = input("Please enter the month you were born: ")
        if month_input.isnumeric() and float(month_input).is_integer() and float(month_input) <= 12:
            get_month = False
            return int(month_input)
        if month_input.isalpha() and month_input.lower() in month_dict.values():
            for month_number, month_string in month_dict.items():
                if month_input.lower() == month_string:
                    get_month = False
                    return month_number
        print("Error: Invalid Character(s) Detected.")

def get_user_day():
    'Prompts user for their birth day'
    get_day = True
    while get_day is True:
        day_input = input("Please enter the day you were born: ")
        if day_input.isnumeric() and float(day_input).is_integer() and float(day_input) <= 31:
            get_day = False
            return int(day_input)
        print("Error: Invalid character(s) detected.")

def get_suffix():
    'Determines suffix on current day'
    if currentDay in (1, 21, 31):
        suffix = "st"
    elif currentDay in (2, 22):
        suffix = "nd"
    elif currentDay in (3, 23):
        suffix = "rd"
    else:
        suffix = "th"
    return suffix

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

month_dict = {
    1 : "january",
    2 : "february",
    3 : "march",
    4 : "april",
    5 : "may",
    6 : "june",
    7 : "july",
    8 : "august",
    9 : "september",
    10 : "october",
    11 : "november",
    12 : "december"
}

month_end_dict = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

if __name__=="__main__":
    main()
