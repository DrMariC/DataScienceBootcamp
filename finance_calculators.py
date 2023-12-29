# This Python programe allows the user to choose between 'investment' and 'bond' calculators, takes relevant inputs based on the choice, and calculates and prints the result accordingly.
# December 2023\

import math

print("Enter either 'investment' or 'bond' to perform calculations:")

user_choice = input("Enter your choice: ")

if user_choice != 'investment' and user_choice != 'bond':
    print("Please choose between 'investment' or 'bond'.")
else:
    
    if user_choice == 'investment':
        # Get user's input for investment
        amount = float(input("Enter the amount of money you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years you plan on investing: "))
        interest_option = input("Enter 'simple' or 'compound' interest: ")

        # Calculate investment amount using the respective formulae
        if interest_option == 'simple':
            investment = amount * (1 + interest_rate * years)
        elif interest_option == 'compound':
            investment = amount * math.pow((1 + interest_rate), years)
        else:
            print("Please enter 'simple' or 'compound'.")

        # Print the result
        print(f"Your investment will be: {round(investment, 2)}")

    # Bond calculation
    elif user_choice == 'bond':
        # Get user's input for bond
        curent_value = float(input("Enter the curent value of the house: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        months = int(input("Enter the number of months you plan to repay the bond: "))

        # Calculate monthly repayment
        i = interest_rate / 12
        bond_repayment = (i * curent_value) / (1 - math.pow((1 + i), -months))

        # Print the resultrounded to 1 decimal place
        print(f"Your monthly bond repayment will be: {round(bond_repayment, 1)}")
