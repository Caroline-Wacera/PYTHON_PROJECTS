#⭐ Exercise 1
#Ask the user for numbers.
#Stop when they type a negative number.
#Print the sum of all numbers typed.
number = int(input("Enter a number:"))
total = 0
while number >= 0:
              total += number 
              number = int(input("Enter a number:"))
print(f"The sum of all numbers types is {total}")


#⭐ Exercise 2
#Ask for a username.
#If it’s wrong → ask again.
#Maximum 3 attempts.
correct_username = "admin"
attempts = 0
while attempts < 3:
    username = input("Enter a username:")
    if username == correct_username:
        print("Access granted")
        break
    else:
        print("Wrong username, try again")
    attempts += 1
if attempts == 3:
    print("Too many attempts, Access denied")


#⭐ Exercise 3
#Print this shape using nested while loops:
#*
#**
#***
#****

i = 1
while i <= 4:
    j = 1
    while j <= i:
        print("*", end="")   # stay on same line
        j += 1
    print()                  # move to next line
    i += 1
