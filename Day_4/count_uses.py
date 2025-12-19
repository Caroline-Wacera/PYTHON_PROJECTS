"""QUESTION 1 — Count Positive Numbers (Basic)
Ask the user to enter numbers until they type -1.
Count how many positive numbers were entered.
Rules
Do not count 0
Do not count -1"""
count = 0
number = 0
while number != -1:
    number = int(input("Enter a number (stop at -1):"))
    if number > 0:
        count += 1
print("Positive numbers are:",count)


""" QUESTION 2 — Count Even Positive Numbers
Ask the user to enter numbers until -1.
Count only positive even numbers.
Hint
Use % (modulo)"""
count = 0
number = 0
while number != -1:
    number = int(input("Enter a number (stop at -1):"))
    if number % 2 == 0 and number > 0:
        count += 1
print("Even positive numbers are:",count)


"""QUESTION 3 — Count Numbers Greater Than 10
Ask the user to enter numbers until -1.
Count how many numbers are greater than 10."""
count = 0
number = 0
while number != -1:
    number = int(input("Enter a number (stop at -1):"))
    if number > 10:
        count += 1
print("The numbers that are greater than 10 are:",count)


"""QUESTION 4 — Count Valid Scores
Ask the user to enter exam scores until -1.
Count how many scores are valid.
Valid score rules
Between 0 and 100 (inclusive)
Ignore negatives (except -1)"""
count = 0
exam_score = 0
while exam_score != -1:
    exam_score = int(input("Enter the exam score (stop at -1):"))
    if exam_score >= 0 and exam_score <= 100:
        count += 1
print("The valid scores are:",count)


""" QUESTION 5 — Count Correct Password Attempts
Ask the user to enter a password until they type "exit".
Count how many times the user enters the correct password.
Rules
Correct password is "python123"
Do not count "exit" """
count = 0
password = ""
while password != "exit":
    password = input("Enter a password:")
    if password == "python123":
        count += 1
print("The Correct Password Attempts are:",count)
