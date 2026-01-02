"""Exercise 1
Start from 1
Keep printing numbers
Stop at 5
Do NOT use break"""
number = 1
while number <= 5:
    print(number)
    number += 1



"""Exercise 2
Ask the user to enter "yes"
Keep asking until they type "yes"
Then print "Correct"""
user_input = ""
while user_input != "yes":
    user_input = input("Enter an input until you enter (yes):")
print("Correct")



"""Exercise 3 — Keep Asking Until Positive
Task:
Ask the user to enter a number.
Keep asking until they enter a positive number (> 0).
Rules:
If number ≤ 0 → print "Not positive, try again"
When positive → print "Thank you!"""
number = int(input("Enter a number:"))
while number <= 0:
    print("Not positive, try again")
    number = int(input("Enter a number:"))
print("Thank you!")



"""Exercise 4 — Count Even Numbers
Task:
Ask the user to enter numbers until they type -1.
Count how many even numbers were entered.
Rules:
Ignore -1
Print the total count at the end"""
count = 0
number = int(input("Enter a number (-1 to stop): "))
while number != -1:
    if number % 2 == 0:
        count += 1
    number = int(input("Enter a number (-1 to stop): "))
print("Total even numbers:", count)



"""Exercise 5 — Simple Login System
Task:
Ask the user to enter a password.
Rules:
Correct password is "admin"
Allow 3 attempts
If correct → print "Access granted"
If all attempts fail → print "Access denied"""
attempts = 0
while attempts < 3:
    password = input("Enter the password: ")
    if password == "admin":
        print("Access granted")
        break
    else:
        attempts += 1
        print(f"Incorrect password. Attempts left: {3 - attempts}")
else:
    print("Access denied")
    
