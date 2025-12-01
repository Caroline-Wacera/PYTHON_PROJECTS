name = "Carol"
age = 30
height = 127.6
is_student = True
favourite_languages = ["English" ,"Swahili" , "French" , "Kikuyu" , "German" ]
favourite_languages.append("Dholuo")
print(favourite_languages)
favourite_languages.remove("German")
print(favourite_languages)
print(name, age, height, is_student)
print(type(age),type(name),type(height),type(is_student),type(favourite_languages))


#Ask the user for their name, age, height, and student status (True/False).
#Print all the information using f-strings.
#Print the data type of each variable.
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
student_status = input("Are you a student?:") == "True"
print(f"Your name is {name}, You are {age} years old, {height} cms tall and your student status is {student_status}")
print(type(name),type(age),type(height),type(student_status))


#Store the data in a dictionary.
person = {"name" :"Carol" ,"age" : 30 ,"height" : 125.7 ,"student_status" : True}
#Print the dictionary and its type using f-strings.
print(f"The data type of dictionary variable person, is {type(person)}")
