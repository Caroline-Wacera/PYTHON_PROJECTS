count = 0
word = "Python"

for letter in word:
    count += 1

print("Length:", count)


for i in range(10, 0, -1):
    print(i)

#Exercise 1:
#Create a list of five fruits.
#Loop through them and print:
#“<fruit> is healthy!”

fruits = ["orange","pinapple","apple","pear","mango"]
for fruit in fruits:
    print(f"{fruit} is healthy")

#Exercise 2:
#Ask the user for a word.
#Use a for-loop to print each character on a new line.
word = input("Enter a word:")
for letter in word:
    print(letter)

#Exercise 3:
#Use range() to print numbers from 10 to 20.
for i in range(10,21):
    print(i)

#Exercise 4:
#Create a list of 4 names.
#Print: "Name at index X is Y" using a loop with indexes.
names = ["Anna", "Brian", "Caroline", "David"]
for i in range(len(names)):
    print(f"Name at index {i} is {names[i]}")

#Exercise 5:
#Using two strings,
#example: "ab" and "12"
#print all possible combinations using nested loops.
letters = "ab"
numbers = "12"
for letter in letters:
    for number in numbers:
        print(letter + number)

