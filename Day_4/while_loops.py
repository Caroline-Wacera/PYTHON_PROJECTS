i = 1

while i <= 5:
    print(i)
    i += 1

#Ask user for input until they type 'stop'
user_input = ""
while user_input != "stop":
    user_input = input("Enter an input:")
print("Correct word")


#Print numbers 1 to 10 using a while loop.
number = 1
while number <= 10:
    print(number)
    number += 1

#Create a countdown from 10 to 1.
count = 10
while count > 0 :
    print(count)
    count -= 1


#Print each letter in your name using a while loop
name = "Caroline"
i = 0
while i < len(name):
    print(name[i])
    i += 1


#Ask the user for a password.
#Keep asking while the password is NOT "python123".
password = ""
while password != "python123":
    password = input("Enter the password:")
print("Correct password")


#Using a list of 5 foods, print each food with index:
foods = ["Pilau","Biryani","Viazi", "Mkate","Mbaazi"]
i = 0
while i < len(foods):
    print(f"Food at index {i} is {foods[i]}")
    i += 1
                   

