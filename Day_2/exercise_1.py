#Exercise 1 — String Slicing
#Ask the user for their full name:
#print the first 3 letters
#print the last 3 letters
#print everything from index 2 to the end
full_name = input("Enter your full name:")
print(full_name[:3])
print(full_name[-3:])
print(full_name[2:])


#Exercise 2 — String Cleanup
#Given a user input that may have extra spaces:
#remove spaces
#convert to lowercase
#print cleaned value using an f-string
favourite_colour = " Yellow "
favourite_colour = favourite_colour.strip()
favourite_colour = favourite_colour.lower()
print(f"my favourite colour is {favourite_colour}")


#Exercise 3 — List Editing
#Create a list of 5 foods. Then:
#replace the 3rd item
#remove the last item
#add one new food using append
#print the final list + type
foods = ["pilau", "chapati", "chicken", "chips", "kachumbari"]
foods[2] = "turkey"
foods.remove("kachumbari")
foods.append("rice")
print(foods)
print(type(foods))


#Exercise 4 — User Profile
#Ask the user:
#name (string)
#age (string → convert to int)
#height (string → convert to float)
#Print with an f-string and show the data type of each.
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height in cms:"))
print(f"My name is {name}, i am {age} years old, and {height} cms tall")
print(type(name) ,type(age) ,type(height))


