#1. Simple If
#Ask the user for a number.
#If the number is positive → print "Positive number"

number = int(input("Enter a number:"))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


#2. If-Else
#Ask the user for a number.
#If the number is even → print "Even"
#Else → print "Odd"

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


#3. If-Elif-Else
#Ask the user for their test score (0–100).
#≥ 90 → print "Excellent"
#≥ 60 → print "Good"
#< 60 → print "Needs Improvement"

test_score = int(input("Enter your test score (0-100):"))
if test_score >= 90:
    print("Excellent")
elif test_score >= 60:
    print("Good")
else:
    print("Needs improvement")


#4. Nested Conditional — Age & Student
#Ask the user for their age and if they are a student (yes/no).
#If age ≥ 18
#If student → print "Adult student"
#Else → print "Adult non-student"
#Else → print "Not an adult"
 
age = int(input("Enter your age:"))
student_status = input("Are you a student?(yes/no):")
if age >= 18:
    if student_status == "yes":
        print("Adult student")
    else:
        print("Adult non-student")
else:
    print("Not an adult")


#5. Nested Conditional — Temperature
#Ask the user for temperature in Celsius.
#If temperature > 30
#If temperature > 35 → print "Very hot"
#Else → print "Hot"
#Else → print "Cool"

temperature = float(input("Enter the temperature:"))
if temperature > 30:
    if temperature > 35:
        print("Very hot")
    else:
        print("Hot")
else:
    print("Cool")


#6. Nested Conditional — Username & Password
#Ask the user for a username and password.
#If username is "admin"
#If password is "1234" → print "Access granted"
#Else → print "Wrong password"
#Else → print "Unknown user"

username = input("Enter the username:")
password = int(input("Enter a password:"))
if username == "admin":
    if password == 1234:
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")


#7. Number Range Checker
#Ask the user for a number.
#If number > 0
#If number < 10 → print "Single digit positive"
#Else → print "Multiple digit positive"
#Else → print "Non-positive number"

number = int(input("Enter a number:"))
if number > 0:
    if number < 10:
        print("Single digit positive")
    else:
        print("Multiple digit positive")
else:
    print("Non-positive number")


#9. Nested Conditional — Trip Eligibility
#Ask the user for age and money they have.
#If age ≥ 18
#If money ≥ 100 → print "You can go on the trip"
#Else → print "Not enough money"
#Else → print "Too young for the trip"

age = int(input("Enter your age:"))
money = int(input("Enter the money you have:"))
if age >= 18:
    if age >= 100:
        print("You can go on the trip")
    else:
        print("Not enough money")
else:
    print("Too young for the trip")


#10. Nested Conditional — Login Simulation
#Ask the user for username and age.
#If username is "Caroline"
#If age ≥ 18 → print "Welcome Caroline"
#Else → print "You are underage"
#Else → print "Unknown user"

username = input("Enter the username:")
age = int(input("Enter your age:"))
if username == "Caroline":
    if age >= 18:
        print("Welcome Caroline")
    else:
        print("You are underage")
else:
    print("Unknown user")








