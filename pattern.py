# This simple Python script prints the requested pattern using if-else statement and two for loops:
print("Example using two for loops: ")
stars = "*"
if stars == "*" : # If we have one star. 
   print(stars)
for i in range(4):
  stars = stars + "*"
  print(stars)
else :
  for i in range(1, 5) :
    index = 5 - i  # i goes from 1 to 5 in this loop
    print(stars[0:index]) 

# This simple Python script prints the requested pattern using if-else statement and a single for loop: 
print("Example using a single for loop: ")
stars = "*"
print(stars)
for i in range(1, 9):
    if i < 5:
        stars += "*"
        print(stars)
    else:
        stars = stars[:-1]
        print(stars)

