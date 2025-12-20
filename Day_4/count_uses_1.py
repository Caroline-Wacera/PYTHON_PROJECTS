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
