"""1️⃣ Keep Asking Until Non-Zero
Ask the user to enter a number.
Keep asking until the number is not zero.
Rules:
If number == 0 → print "Zero not allowed"
Else → print "Accepted"""
number = int(input("Enter a number: "))
while number == 0:
    print("Zero not allowed")
    number = int(input("Enter a number: "))
print("Accepted")



"""2️⃣ Keep Asking Until Even
Ask the user to enter a number.
Keep asking until the number is even.
Rules:
If odd → print "Not even, try again"
If even → print "Thank you!"""
number =int(input("Enter a number:"))
while number % 2 != 0:
    print("Not even, try again")
    number =int(input("Enter a number:"))
print("Thank you!")



"""3️⃣ Keep Asking Until Within Range
Ask the user to enter a number.
Keep asking until the number is between 1 and 10 (inclusive).
Rules:
If outside range → print "Out of range"
If valid → print "Correct"""
number =int(input("Enter a number:"))
while number < 1 or number > 10:
    print("Out of range")
    number =int(input("Enter a number:"))
print("Correct")



"""4️⃣ Keep Asking Until Correct Word
Ask the user to enter a word.
Keep asking until they type "yes".
Rules:
If wrong → print "Try again"
If correct → print "Correct"""
word = ""
while word != "yes":
    print("Try again")
    word = input("Enter a word:")
print("Correct")



"""5️⃣ Keep Asking Until Minimum Length
Ask the user to enter a password.
Keep asking until the password has at least 6 characters.
Rules:
If too short → print "Password too short"
Else → print "Password accepted"""

