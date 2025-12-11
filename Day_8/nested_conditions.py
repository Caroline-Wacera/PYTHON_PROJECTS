""" #1️⃣ Ask user for username, password, and role.
Allow login ONLY if:
username is "root"
password is "1234"
role is "admin" """
username = input("Enter a username:")
password = input("Enter a password:")
role = input("Enter a role:")
if username == "root":
    if password == "1234":
        if role == "admin":
            print("Log in successful")
        else:
            print("Log in failed,try again!")
    else:
        print("Log in failed,try again!")
else:
    print("Log in failed,try again!")



""" 2️⃣ Ask user for age and country.
Permit access ONLY if:
age ≥ 21
country is "Kenya"
AND they say “yes” to having a passport."""
age = int(input("Enter an age:"))
country = input("Enter a country:")
passport_ownership = input("Do you have a passport:")
if age >= 21:
    if country == "Kenya":
        if passport_ownership == "yes":
            print("Access granted")
        else:
            print("Access denied")
    else:
        print("Access denied")
else:
    print("Access denied")


"""3️⃣ Mpesa-like flow:
Ask for amount, balance, and PIN.
Allow transaction only if:
amount ≤ balance
PIN is correct
Else show appropriate errors."""
amount = int(input("Enter the amount: "))
balance = int(input("Enter the balance: "))
pin = input("Enter the pin: ")

if amount <= balance:
    if pin == "1234":
        print("Transaction allowed")
    else:
        print("Incorrect PIN")
else:
    print("Insufficient balance")



"""4️⃣ Shopping discount system:
Ask for:
Has coupon? (yes/no)
Is VIP member? (yes/no)
Rules:
If VIP → automatic 20% discount
If coupon → 10%
If both → 30%"""
if vip_member == "yes":
    if has_coupon == "yes":
        print("Discount is 30%")     # VIP + coupon
    else:
        print("Discount is 20%")     # VIP only
else:
    if has_coupon == "yes":
        print("Discount is 10%")     # Coupon only
    else:
        print("No discount")         # None



"""5️⃣ Student exam grading system:
Ask:
exam score
project submitted? (yes/no)
Rules:
If score ≥ 50 AND project submitted → pass
If score ≥ 50 BUT project not submitted → “Submit project”
If score < 50 → fail"""
exam_score = int(input("Enter the exam score:"))
project_submition = input("Have you submitted the project?")
if exam_score >= 50:
    if project_submition == "yes":
        print("Pass")
    else:
        print("Submit project")
else:
    print("Fail")
