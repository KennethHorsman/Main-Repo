def determine_leap_year():
    'Determines if birth year was a leap year'
    year = int(input("Enter year: "))
    leap_year = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    if year % 100 != 0:
        if year % 4 == 0:
            leap_year = True
    return leap_year

leapyear = determine_leap_year()
print(leapyear)