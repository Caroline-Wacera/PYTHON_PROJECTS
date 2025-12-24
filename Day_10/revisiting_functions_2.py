"""Create a function check_number
Takes one number
If number > 0 → print "Positive"
Else → print "Not positive"
Call the function"""
def check_number(number):
    if number > 0:
        print("Positive")
    else:
        print("Not positive")
check_number(4)



"""👉 Create a function even_or_odd
👉 Takes one number
👉 Prints "Even" or "Odd"
👉 Call the function with 7"""
def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_or_odd(7)



"""👉 Create a function square
👉 Takes one number
👉 Returns the square
👉 Print the returned value"""
def square(number):
    return number * number
result = square(4)
print(result)



"""👉 Function pass_fail(score)
👉 If score ≥ 50 → print "Pass"
👉 Else → print "Fail"
👉 Call with 45"""
def pass_fail(score):
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
pass_fail(45)



"""👉 Function login(username)
👉 If username is "admin" → print "Welcome"
👉 Else → print "Access denied"
👉 Call the function"""
def login(username):
    if username == "admin":
        print("Welcome")
    else:
        print("Access denied")
login("Caroline")



"""👉 Function guess_yes()
👉 Allow 2 attempts
👉 If user types "yes" → print "Correct" and stop
👉 Else after attempts → "Failed"""
def guess_yes():
