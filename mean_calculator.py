# This simple Python program is using a while loop to continually ask the user to enter a number (unless the entered number is -1) and prints the mean:

# Declare variables
sum = 0
count = 0

# Continuously ask the user to enter a number
while True:
    user_input = input("Enter as many numbers as you like, once finished, enter -1 to stop and calculate the mean: ")
    # Check if the user wants to stop
    if user_input == "-1":
        break

    # Check if the input is an integer
    if user_input != int():
        number = int(user_input)
        sum += number
        count += 1
    else:
        print("Please enter an integer.")

# Calculate the mean but avoid division by zero!
if count > 0:
    mean = sum / count
    print(f"The mean of the entered integers is: {mean}")
else:
    print("No integers entered.")


    
