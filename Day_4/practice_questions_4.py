#Print numbers from 3 to 30, counting by 3.
#📌 Use a while loop
number = 3
while number <= 30:
    print(number)
    number += 3


#2️⃣ Stop at Zero
#Ask the user for numbers.
#Keep asking until the user enters 0.
#When they enter 0, print:
number = int(input("Enter a number:"))
while number != 0:
    print(number)
    number = int(input("Enter a number:"))
print("You entered 0, stopping!")


#3️⃣ Skip a Number
#Print numbers from 1 to 10, but skip 7.
#📌 Use if inside the loop
number = 1
while number <= 10:
    if number == 7:
        number += 1
        continue
    print(number)
    number += 1


#4️⃣ Limited Attempts
#Ask the user for a password.
#Allow 3 attempts only.
#If correct password is "python" → print "Access granted"
#If attempts finish → print "Locked out"
count = 0
while count < 3:
    password = input("Enter a password: ")
    if password == "python":
        print("Access granted")
        break               # Stop asking if correct
    else:
        print("Wrong password")
    count += 1
else:
    print("Locked out")


#5️⃣ Running Total
#Ask the user to enter numbers.
#Keep adding them.
#Stop when the user enters -1.
#Print the total sum.
total = 0           # Initialize running total
number = 0          # Initialize number to enter the loop
while number != -1:   # Keep looping until user enters -1
    number = int(input("Enter a number (-1 to stop): "))
    if number != -1:  # Only add if it’s not the stopping value
        total += number
print("Total sum:", total)
