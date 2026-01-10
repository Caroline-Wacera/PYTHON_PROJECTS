#1️⃣ Print Numbers
#Write a program that prints numbers from 1 to 10 using a for loop.
for number in range(1, 11):
    print(number)



#2️⃣ Print Even Numbers
#Print all even numbers between 1 and 20.
for number in range(1, 21):
    if number % 2 == 0:
        print(number)


#3️⃣ Count Down
#Print numbers from 10 down to 1.
for number in range(10, 0, -1):
    print(number)


#4️⃣ Sum of Numbers
#Ask the user for a number n
#Print the sum of numbers from 1 to n.
n =int(input("Enter a number:"))
total = 0
for number in range(1, n + 1):
    total += number 
print("sum", total)
