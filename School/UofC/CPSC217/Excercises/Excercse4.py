#  CPSC 217 Exercise 4: Display a message that includes ordinal numbers
# Kenneth Horsman (UCID: 30260797)

def int2ordinal(integer):
  last_digit = integer % 100
  suffix_dict = {(11,12,13) : "th", 1 : "st", 2 : "nd", 3 : "rd"} # Apparently only using a tuple will work for the first key, not a list

  if last_digit in suffix_dict:
    return f"{integer}{suffix_dict[last_digit]}"
  else:
    return f"{integer}th"

###############################################################################
#
#  Don't change any code below this point in the file.
#
###############################################################################

# Demonstrate the int2ordinal function by reading a day, month and year and
# displaying the entered values as ordinal numbers as part of a longer message.
def main():
  day = int(input("Enter a day between 1 and 31: "))
  month = int(input("Enter a month between 1 and 12: "))
  year = int(input("Enter a year between 1 and 2100: "))

  print("On the", int2ordinal(day), "day of the", int2ordinal(month), \
        "month of the", int2ordinal(year), "year, something amazing happened!")

# Call the main function
main()