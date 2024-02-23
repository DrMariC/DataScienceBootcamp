# This simple Python program reads in a string and makes each alternate character into an upper case character and each other alternate character into a lower case character.
# It then makes each alternative word upper and lower case.

# Declare variables
my_string = "how are you there?"
my_alternate_chars_string = ""
my_alternate_words_string = ""
my_alternate_words_string_odd = "" # RESUBMISSION: As per reviewer's arvise, declaring a variable to which I would add the modified words.
my_alternate_words_string_even = ""

# Loop through each character in the given string and make every odd to lower and every even to upper case
for i in range(len(my_string)):
    if i % 2 != 0:
        my_alternate_chars_string += my_string[i].lower()
    else:
        my_alternate_chars_string += my_string[i].upper()
    i += 1
print(my_alternate_chars_string) 

# Split the initial string into separate words and save as a list 
my_string_split = my_string.split(" ")
# Loop through every element in a list and make every odd to upper and every even to lower case words
# # RESUBMISSION: As per reviewer's arvise, using the same logic as above and adding  a blank space to my string
for i in range(len(my_string_split)):
    if i % 2 != 0: 
        my_alternate_words_string += " " + my_string_split[i].upper()
    else:
        my_alternate_words_string += " " + my_string_split[i].lower()
i += 1
print(my_alternate_words_string)