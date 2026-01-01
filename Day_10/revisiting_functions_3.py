"""1️⃣ check_temperature
Create a function check_temperature
Takes one number (temperature)
If temperature ≥ 37 → print "Fever"
Else → print "Normal"
Call the function with 36"""
def check_temperature(temperature):
    if temperature >= 37:
        print("Fever")
    else:
        print("Normal")
check_temperature(36)



"""2️⃣ is_positive
Create a function is_positive
Takes one number
If number > 0 → print "Positive"
Else → print "Zero or Negative"
Call the function with -3"""
def is_positive(number):
    if number > 0:
        print("Positive")
    else:
        print("Zero or Negative")
is_positive(-3)



"""3️⃣ greet_user
Create a function greet_user
Takes one parameter (name)
Prints: "Hello, NAME"
Call it with "Caroline"""
def greet_user(name):
    print("Hello", name)
greet_user("Caroline")



"""4️⃣ multiply_by_five
Create a function multiply_by_five
Takes one number
Prints the number multiplied by 5
Call it with 6"""
def multiply_by_five(number):
    print(number * 5)
multiply_by_five(6)



"""5️⃣ check_voting
Create a function check_voting
Takes age
If age ≥ 18 → print "Eligible to vote"
Else → print "Not eligible"
Call it with 17"""
def check_voting(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible")
check_voting(17)
