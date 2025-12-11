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
amount = int(input("Enter the amount:")
