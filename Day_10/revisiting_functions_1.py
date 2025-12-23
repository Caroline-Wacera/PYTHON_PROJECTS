"""👉 Write a function called greet
👉 It should print "Welcome!"
👉 Call the function once"""
def greet():
    print("Welcome")
greet()


"""👉 Write a function called ask_name
👉 Ask the user for their name
👉 Print: "Hello, NAME"""
def ask_name():
    name = input("Enter your name:")
    print("Hello",name)
ask_name()


"""👉 Write a function called triple
👉 It takes one number
👉 Prints the number multiplied by 3
👉 Call it with 5"""
def triple(number):
    print(number * 3)
triple(5)


"""👉 Write a function called cube
👉 Takes one number
👉 Returns the number cubed
👉 Print the result
📌 Formula reminder:
cube = number × number × number"""
def cube(number):
    return number * number * number
result = cube(3)
print(result)
#3 has been assigned as a values i.e number = 3. I could use any other value.


"""👉 Write a function called check_age
👉 Takes one number (age)
👉 If age ≥ 18 → print "Adult"
👉 Else → print "Minor"
👉 Call the function"""
def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

check_age(20)
