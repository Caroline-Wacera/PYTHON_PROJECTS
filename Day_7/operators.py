#Ask the user for age and nationality.
#If age ≥ 18 and nationality is "Kenyan", print “Eligible”.
age = int(input("Enter your age:"))
nationality = input("Enter your nationality:")
if age >= 18 and nationality == "Kenyan":
    print("Eligible")



#Ask user for username and password.
#If username == "root" or username == "admin", print “Special access”.
username = input("Enter a username:")
paasword = input("Enter a password:")
if username == "root" or username == "admin":
    print("Special access")



#Ask user for email_verified (True/False).
#If not email_verified, print “Please verify email”.
email_verified = input("Is your email verified? (True/False):")
if email_verified == "False":
    print("Please verify email")



#Ask for two numbers.
#If both are positive, print “Both positive”.
#If at least one is positive, print “At least one positive”.
number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
if number_1 > 0 and number_2 > 0:
    print("Both positive")
elif number_1 > 0 or number_2 > 0:
    print("At least one positive")



#Ask for a number.
#If number > 0 and number < 100, print “Valid range”.
number = int(input("Enter a number:"))
if number > 0 and number < 100:
    print("Valid range")
