# Print numbers from 10 down to 1 using a while loop
numbers = 10
while numbers >= 1:
    print(numbers)
    numbers -= 1


#1️⃣ Counting Up
#Print numbers from 1 to 10 using a while loop.
number = 1 
while number <= 10:
    print(number)
    number += 1

#2️⃣ Counting Down
#Print numbers from 20 down to 10 using a while loop.
number = 20
while number >= 10:
    print(number)
    number -= 1

#3️⃣ Repeat Message
#Print "Hello World" exactly 5 times using a while loop.
word = "Hello World"
count = 0
while count < 5:
    print(word)
    count += 1

#4️⃣ Ask Until Correct
#Ask the user for a password.
#Keep asking while the password is not "python".
#When correct, print "Access granted".
password = input("Enter a password:")
while password != "python":
    print(password)
    password = input("Enter a password:")
print("Access granted")


#5️⃣ User Exit Control
#Ask the user to type something.
#Keep asking while the user does not type "quit".
#When they type "quit", print "Program ended".
something = input("Type something:")
while something != "quit":
    print(something)
    something = input("Type something:")
print("Program ended")
