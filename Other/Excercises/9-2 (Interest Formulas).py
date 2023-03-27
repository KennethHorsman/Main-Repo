#pylint: disable=line-too-long
'''
2a. Create the logic for a program that calculates and displays the amount of money you would have if you 
invested $5000 at 2 percent simple interest for one year. Create a separate method to do the calculation and return the result to be displayed.

2b. Modify the program in Exercise 2a so that the main program prompts the user for the amount of money and passes it to the interest-calculating method.

2c. Modify the program in Exercise 2b so that the main program also prompts the user for the interest rate 
and passes both the amount of money and the interest rate to the interest-calculating method.
'''

def main():
    'Takes user input, then calculates and displays the money returned on an investment.'
    print("This program calculates the money returned on any investment. Please follow the steps below.")
    investment_return = calculate_investment_return()
    print(f"The money returned on your investment is ${investment_return:,.2f}")

def calculate_investment_return():
    'Calculates interest based on user input'
    e = 2.71828
    principal_balance = get_principal_balance()
    interest_rate = get_interest_rate()
    years = get_num_years()
    formula = get_interest_formula("Please enter \'A\' for SIMPLE interest, \'B\' for COMPOUND interest, or \'C\' for CONTINUOUS interest: ")
    if formula == 'A':
        calculation = principal_balance * (1 + (interest_rate * years))
    if formula == 'B':
        compounds = get_num_compounds()
        calculation = principal_balance * (1 + (interest_rate / compounds))**(compounds * years)
    if formula == 'C':
        calculation = principal_balance * e**(interest_rate * years)
    return calculation

def get_interest_formula(prompt):
    'Asks user which formula they would like to use'
    formula = input(prompt)
    while formula not in ('A', 'B', 'C'):
        print("Error: Invalid Character(s) Detected.")
        formula = input(prompt)
    return formula

def get_principal_balance():
    'Prompts user for principal balance'
    principal_balance = get_non_negative_number("Please enter your principal balance: $")
    return principal_balance

def get_interest_rate():
    'Prompts user for interest rate'
    interest_rate = get_non_negative_number("Please enter your interest rate as a whole number:")
    while not interest_rate.is_integer():
        print("Error: Please enter a whole number.")
        interest_rate = get_non_negative_number("Please enter your interest rate as a whole number:")
    return (interest_rate / 100)

def get_num_years():
    'Prompts user for number of years'
    years = get_non_negative_number("Please enter the number of years: ")
    while not years.is_integer():
        print("Error: Please enter a whole number.")
        years = get_non_negative_number("Please enter the number of years: ")
    return years

def get_num_compounds():
    'Prompts user for number of compounds'
    compounds = get_non_negative_number("Please enter the number of compounding periods per year: ")
    while not compounds.is_integer():
        print("Error: Please enter a whole number.")
        compounds = get_non_negative_number("Please enter the number of compounding periods per year: ")
    return compounds  

def get_non_negative_number(prompt):
    'Returns user_input once it is a positive, valid number'
    user_input = input(prompt)
    while not is_valid_number(user_input):
        print("Error: Invalid Character(s) Detected.")
        user_input = input(prompt)
    while float(user_input) <= 0:
        print("Please enter a positive number.")
        user_input = input(prompt)
    return float(user_input)

def is_valid_number(num):
    'Determines if num can be converted to a float'
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
