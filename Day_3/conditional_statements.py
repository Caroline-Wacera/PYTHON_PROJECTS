#Ask the user for a number.
#If number > 10 → print "Big number"
#Else → print "Small number"
number = int(input("Enter a number:"))
if number > 10:
    print("Big number")
else:
    print("Small number")


#Ask the user for a character.
#If it’s 'a' → print "First letter of alphabet"
#Else if it’s 'z' → print "Last letter of alphabet"
#Else → print "Other letter"
character = input("Enter a character:")
if character == "a":
    print("First letter of alphabet")
elif character == "z":
    print("Last letter of alphabet")
else:
    print("Other letters")


