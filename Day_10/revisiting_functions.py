"""👉 Write a function called hello
👉 It should print "Hello World"
👉 Call it once"""
def hello ():
    print("Hello World")
hello()


"""👉 Write a function called ask_age
👉 Ask the user for their age
👉 Print: "You are X years old"""
def ask_age ():
    age = input("What is your age?:")
    print(f"You are {age} years old")
ask_age()


"""👉 Create a function double
👉 It takes one number
👉 Prints the number multiplied by 2"""
def double(number):
    print(number * 2)
double(4)


"""👉 Create a function square
👉 Takes one number
👉 Returns the square
👉 Print the result"""
def square(number):
    return number * number
result =square(4)
print(result)
