#Write a program that keeps asking the user for the password until they enter "python123".
password =input("Enter the password:")
while password != "python123":
    password =input("Enter the password:")
print("Right password")


#Ask the user for a number, then count down to 0.
number =int(input("Enter a number:"))
while number >= 0:
    print(number)
    number -= 1


#Keep asking the user for numbers.
#Stop only when they type "stop" and print the total.
total = 0
number = ""
while number != "stop":
    number = input("Enter a number or 'stop': ")
    if number != "stop":
        total += int(number)
print("Total =", total)


#The user has to guess the number 7.
#Give hints:
#“Too low”
#“Too high”
number = 7
guess = int(input("Enter a number:"))
while guess != 7:
    guess = int(input("Enter a number:"))
    if guess < 7:
        print("Too low")
    else:
        print("Too high")
print("Correct number")


#Ask the user for a username.
#If it’s less than 5 characters, ask again.
username = input("Enter a username: ")
while len(username) < 5:
    print("Username too short! Must be at least 5 characters.")
    username = input("Enter a username: ")
print("Username accepted:", username)
