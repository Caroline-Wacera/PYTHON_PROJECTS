#Print numbers from 1 to 10, but skip 5.
#📌 Hint: Use if inside the loop.
number = 1
while number <= 10:
    if number == 5:
        number += 1
        continue
    print(number)
    number += 1


#2️⃣ Count Even Numbers
#Print only even numbers from 1 to 20 using a while loop.
numbers = 1
while numbers <= 20:
    if numbers % 2 == 0:
        print(numbers)
    numbers += 1


#Ask the user for a number.
#Keep counting from 1 upward until you reach that number.
number = int(input("Enter a number: "))
count = 1
while count <= number:
    print(count)
    count += 1


#Ask the user for a number n.
#Use a while loop to calculate the sum from 1 to n.
n = int(input("Enter a number: "))
total = 0
count = 1
while count <= n:
    total += count
    count += 1
print("Sum:", total)


#Count down from 5 to 1, then print:
#Boom! 🚀
number = 5
while number >= 1:
    print(number)
    number -= 1
print("Boom! 🚀")
