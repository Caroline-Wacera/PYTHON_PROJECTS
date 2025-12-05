def greet():
    print("Hello Caroline")

greet()

def greet(name):
    print(f"Hello {name}!")

greet("Wacera")
greet("Caroline")


#Write a function called greet() that prints:
#Hello, welcome!
def greet():
    print("Hello, welcome")
greet()


#Write a function say_hello(name) that prints:
#Hello <name>!
#Ask the user for their name and pass it to the function.
def say_hello(name):
    print(f"Hello, {name}!")

name = input("Enter your name:")
say_hello(name)


#Write a function add(a, b) that prints the sum of two numbers given by the user.
def add(a,b):
    print(a + b)
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
add(a,b)


#Write a function square(num) that returns the square of the number.
#Print the returned value.
def square(num):
    return num * num
num = int(input("Enter a number:"))
answer = square(num)
print(answer)


#Write a function user_profile(name, age) that prints a formatted message like:
#Name: <name>, Age: <age>
#Then call this function using user input.
def user_profile(name, age):
    print(f"Name: {name}, Age: {age}")
name = input("Enter a name:")
age = int(input("Enter an age:"))
user_profile(name,age)


#Write a function check_age(age):
#If age ≥ 18 → print “Adult”
#Else → print “Minor”
#Call the function.
def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
age = int(input("Enter an age:"))
check_age(age)


#Write a function bmi(weight, height) that returns the BMI value.
#Print the result outside the function.
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    return bmi_value 
weight = float(input("Enter the weight in kgs:"))
height = float(input("Enter the height in meters:"))
bmi_result = bmi(weight, height)
print(f"The BMI value is {bmi_result}")


#Write a function:
#def greet_user(name="Guest"):
#And print:
#Hello <name>
#Call it with a name AND without a name.
def greet_user(name="Guest"):
    print(f"Hello, {name}")
greet_user("Caroline")
greet_user()


#a function multiply(a, b) that returns the product
#another function show_result() that calls multiply and prints the result
def multiply(a, b):
    return a * b
def show_result():
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    result = multiply(a, b)
    print(f"The product is {result}")
show_result()


#Write a function clean_text(text) that:
#strips spaces
#converts to lowercase
#returns the cleaned value
#Ask the user for a word, clean it using the function, and print the result.
def clean_text(text):
    value = text.strip()
    cleaned_value = value.lower()
    return cleaned_value
word = input("Enter a word:")
cleaned_word = clean_text(word)
print(f"The cleaned word is: {cleaned_word}")
