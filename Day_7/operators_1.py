#Ask the user for their temperature.
#If temperature is greater than or equal to 36 AND less than or equal to 37.5, print “Normal temperature”
#If temperature is greater than 37.5, print “Fever”
#If temperature is less than 36, print “Low temperature”
temperature = float(input("Enter your temperature:"))
if temperature >= 36 and temperature <= 37.5:
    print("Normal temperature")
elif temperature > 37.5:
    print("Fever")
else:
    print("Low temperature")


"""#1️⃣ Username Check
Create a list:
users = ["caroline", "mark", "susan", "kevin"]
Ask the user for a username.
If the username exists in users, print "User found"
Else print "User not found" """
users = ["caroline", "mark", "susan", "kevin"]
username = input("Enter a username:")
if username in users:
    print("User found")
else:
    print("User not found")


""" 2️⃣ Email Validation
Ask the user for an email.
If the email contains "@", print "Valid email"
Else print "Invalid email" """
email = input("Enter an email:")
if "@" in email:
    print("Valid email")
else:
    print("Invalid email")



"""3️⃣ Check If Number Exists
Given:
numbers = [4, 7, 10, 20, 25]
Ask the user for a number.
If that number is in the list, print "Exists"
Else print "Not in list" """
numbers = [4, 7, 10, 20, 25]
number = int(input("Enter a number:"))
if number in numbers:
    print("Exists")
else:
    print("Not in list")



"""4️⃣ Password Strength
Ask the user to enter a password.
If the password contains any one of these characters:
!  @  #
Print "Strong password"
Else print "Weak password" """
password = input("Enter a password:")
if "!" in password or "@" in password or "#" in password:
    print("Strong password")
else:
    print("Weak password")


"""5️⃣ Restricted Countries
List:
restricted = ["Somalia", "North Korea", "Syria"]
Ask for a country.
If the country is in restricted, print "Access denied"
Else print "Access granted" """
restricted = ["Somalia", "North Korea", "Syria"]
country = input("Enter a country:")
if country in restricted:
    print("Access denied")
else:
    print("Access granted")



""" 6️⃣ Letter Search
Ask the user to enter a word, then a letter.
If the letter is in the word, print "Letter found"
Else print "Letter not found" """
word = input("Enter a word:")
letter = input("Enter a letter:")
if letter in word:
    print("Letter found")
else:
    print("Letter not fount")



"""7️⃣ Login Validation
Allowed usernames:
allowed = ["admin", "root", "superuser"]
Ask for a username.
If username is not in the list, print "Unauthorized user"
Else print "Welcome" """
allowed = ["admin", "root", "superuser"]
username = input("Enter a username:")
if username in allowed:
    print("Unauthorized user:")
else:
    print("Welcome")


"""8️⃣ Vowel Check
Ask the user to enter a letter.
If the letter is in "aeiou", print "Vowel
Else print "Not a vowel" """
letter = input("Enter a letter:")
if letter in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")



""" 9️⃣ Shopping Cart Item Check
Given:
cart = ["bread", "milk", "eggs"]
Ask the user for an item.
If the item is in cart, print "Item already added"
Else print "Item not in cart" """
cart = ["bread", "milk", "eggs"]
item = input("Enter an item:")
if item in cart:
    print("Item already added")
else:
    print("Item not in cart")


"""🔟 PIN Blacklist
Blacklisted PINs:
blacklist = ["0000", "1234", "1111"]
Ask user for a PIN.
If the PIN is in blacklist, print "PIN not allowed"
Else print "PIN accepted" """
blacklist = ["0000", "1234", "1111"]
pin = input("Enter a pin:")
if pin in blacklist:
    print("PIN not allowed")
else:
    print("PIN accepted")
