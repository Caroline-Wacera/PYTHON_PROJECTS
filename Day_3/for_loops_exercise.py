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


#5️⃣ Multiply by 5
#Print the multiplication table of 5 (from 1 to 10).
for number in range(1, 11):
    print(5 * number)


#6️⃣ Skip a Number
#Print numbers from 1 to 10, but skip number 5.
for i in range(1, 11):
    if i != 5:
        print(i)


#7️⃣ Count Evens
#Count how many even numbers are between 1 and 50.
count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1

print("Total even numbers:", count)


#8️⃣ Print Odd Numbers
#Print all odd numbers from 1 to 15.
for number in range(1, 16):
    if number % 2 != 0:
        print(number)


#9️⃣ Repeat Word
#Ask the user for a word.
#Print it 5 times using a for loop.
word = input("Enter a word:")
for i in range(5):
    print(word)
