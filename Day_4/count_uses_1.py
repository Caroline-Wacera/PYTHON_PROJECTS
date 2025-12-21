"""🟢 Practice 1 (Very Easy)
Allow 2 attempts to guess "yes".
Rules:
If correct → print "Correct"
If failed → "Out of attempts"""
attempts = 0
success = False
while attempts < 2:
    guess = input("Guess an input: ")
    if guess == "yes":
        print("Correct")
        success = True
        break
    attempts += 1
if not success:
    print("Out of attempts")


"""🟡 Practice 2 (Easy)
Allow 3 attempts to enter PIN "4321"
Rules:
Correct → "Transaction allowed"
Wrong → "Wrong PIN"
After 3 failures → "Card blocked"""
attempts = 0
correct = False
while attempts < 3:
    pin = input("Enter the pin: ")
    if pin == "4321":
        print("Transaction allowed")
        correct = True
        break
    else:
        print("Wrong PIN")
    
    attempts += 1
if not correct:
    print("Card blocked")


"""🟠 Practice 3 (Medium)
Ask for password "admin123"
Rules:
3 attempts
Print "Attempts left: X" after each failure
Lock after 3"""
attempts = 0
while attempts < 3:
    password = input("Enter a password:")
    if password == "admin123":
        print("Correct password")
        break
    else:
        print("Attempts left:", 3 - attempts)
    attempts += 1
if attempts == 3:
    print("Locked")


"""🔴 Practice 4 (Real-World)
Mpesa-style PIN:
Rules:
PIN = "1111"
Max attempts = 3
If correct → stop immediately
If wrong → count attempts
After lock → "Try again after 24 hours"""
attempts = 0
while attempts < 3:
    pin = input("Enter your PIN: ")
    if pin == "1111":
        print("PIN accepted")
        break
    else:
        attempts += 1
if attempts == 3:
    print("Try again after 24 hours")


"""🔥 Practice 5 (Challenge)
Admin login:
Conditions:
Username must be "admin"
Password must be "root123"
3 attempts TOTAL
Count failed attempts (username OR password)"""
attempts = 0
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "root123":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Wrong credentials")
if attempts == 3:
    print("Account locked")
