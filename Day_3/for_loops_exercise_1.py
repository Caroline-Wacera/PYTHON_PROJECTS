#1️⃣ Print Numbers
#Print numbers from 1 to 5 using a for loop.
for number in range(1, 6):
    print(number)


#2️⃣ Repeat Message
#Print "Python is fun" 3 times using a for loop.
sentence = "Python is fun"
for i in range(3):
    print(sentence)


#3️⃣ Print Even Numbers
#Print all even numbers between 1 and 10.
for number in range(1, 11):
    if number % 2 == 0:
        print(number)


#4️⃣ Print Odd Numbers
#Print all odd numbers between 1 and 15.
for number in range(1, 16):
    if number % 2 != 0:
        print(number)


#5️⃣ Count Up
#Print numbers from 5 to 10.
for number in range(5, 11):
    print(number)


#6️⃣ Skip a Number
#Print numbers from 1 to 10, but skip 6.
for number in range(1, 11):
    if number != 6:
        print(number)


#7️⃣ Count Evens
#Count how many even numbers are between 1 and 20.
#Print the count.
count = 0
for number in range(1, 21):
    if number % 2 == 0:
        count += 1
print(f"The even numbers between 1 and 20 is {count}")


#8️⃣ Count Odds
#Count how many odd numbers are between 1 and 20.
#Print the count.
count = 0
for number in range(1, 21):
    if number % 2 != 0:
        count += 1
print(f"The odd numbers between 1 and 20 is {count}")


#9️⃣ Sum of Numbers
#Calculate the sum of numbers from 1 to 10.
#📌 Use a variable like total
total = 0
for number in range(1, 11):
    total += number
print(f"The sum of numbers from 1 to 10 is {total}")


#🔟 Multiply Table
#Print the multiplication table of 4 (from 1 to 10).
for number in range(1, 11):
    print(number * 4)
    
