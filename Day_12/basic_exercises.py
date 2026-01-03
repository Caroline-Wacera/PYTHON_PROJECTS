"""1️⃣ Keep Asking Until Within Range
Ask the user to enter a number.
Keep asking until the number is between 1 and 10 (inclusive).
Rules:
If outside range → print "Out of range"
If valid → print "Correct"""
number = int(input("Enter a number: "))
while number < 1 or number > 10:
    print("Out of range")
    number = int(input("Enter a number: "))
print("Correct")



"""2️⃣ Keep Asking Until Non-Zero
Ask the user to enter a number.
Keep asking until the number is not zero.
Rules:
If number == 0 → print "Zero not allowed"
Else → print "Accepted"""
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print("Zero not allowed")
    else:
        print("Accepted")
        break



"""3️⃣ Keep Asking Until Even
Ask the user to enter a number.
Keep asking until the number is even.
Rules:
If odd → print "Not even, try again"
If even → print "Thank you!"""
while True:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Thank you!")
        break
    else:
        print("Not even, try again")



"""4️⃣ Password Retry
Ask the user to enter a password.
Keep asking until the password is "admin".
Rules:
If wrong → print "Wrong password"
If correct → print "Access granted"""
while True:
    password = input("Enter password: ")
    if password == "admin":
        print("Access granted")
        break
    else:
        print("Wrong password")



"""5️⃣ Count Attempts
Ask the user to enter a number greater than 100.
Rules:
Count how many wrong attempts were made
If number ≤ 100 → print "Too small"
When valid → print "Accepted after X attempts"""
attempts = 0
while True:
    number = int(input("Enter a number greater than 100: "))
    if number <= 100:
        attempts += 1
        print("Too small")
    else:
        print(f"Accepted after {attempts} attempts")
        break


"""6️⃣ Sentinel Value (-1)
Ask the user to enter numbers.
Stop when they enter -1.
Rules:
Count how many numbers were entered (exclude -1)
Print the total count"""
count = 0
while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    else:
        count += 1
print(f"Total numbers entered: {count}")
