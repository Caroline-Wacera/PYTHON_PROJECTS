#Print numbers from 2 to 20, counting by 2.
number = 2 
while number <= 20:
    print(number)
    number += 2


#Ask the user for a number.
#Print numbers from 1 up to that number.
number =int(input("Enter a number:"))
count = 1
while count <= number:
    print(count)
    count += 1


#Ask the user for a number.
#Count down to 1.
number =int(input("Enter a number:"))
while number >= 1:
    print(number)
    number -= 1


#Ask the user for a number n.
#Calculate and print the sum from 1 to n.
#Ask the user for a number n.
#Use a while loop to calculate the sum from 1 to n.
n = int(input("Enter a number: "))
total = 0
count = 1
while count <= n:
    total += count
    count += 1
print("Sum:", total)


#Ask the user for a word and a number.
#Print the word that many times.
word = input("Enter a word:")
number = int(input("Enter a number:"))
count = 1
while count <= number:
    print(word)
    count += 1
