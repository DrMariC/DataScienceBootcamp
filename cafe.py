# This simple Python program calculates and displays the total stock worth of items on the menu of a hypothetical cafe.

# Create a list for menu with at least four items in it.
menu = ["fruit", "sandwitch", "coffee", "tea"] 

# Create a dictionary that contains the stock value for each item on the menu (keep numbers simple for avoiding logic errors by comparing answers to the manual calculations).
stock = {"fruit" : 4 ,
         "sandwitch" : 3 ,
         "coffee" : 2,
         "tea" : 1}

# Create another dictionary containing prices per item in the stock (again, numbers are intentionaly kept simple).
price = {"fruit" : 1 ,
         "sandwitch" : 3 , 
         "coffee" : 2 ,
         "tea" : 2}

# Initiate a variable to keep track of the total stock worth.
total_stock_worth = 0 

# Loop through the menue list and multiply stock by price for each item.
for i in menu :
    item_value = stock[i] * price[i]
    total_stock_worth += item_value

# Display the resulting value for the total stock worth.
print(total_stock_worth)