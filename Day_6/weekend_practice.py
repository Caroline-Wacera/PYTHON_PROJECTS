#Keep Asking Until User Enters an Even Number
number = int(input("Enter a number:"))
while number % 2 != 0:
    number = int(input("Enter a number:"))
print(f"The number {number} is even")


#Print numbers 1–10, but skip odd numbers using continue.
number = 1
while number <= 10:
    if number % 2 != 0:
        number += 1
        continue 
    print(number)
    number += 1


#Make a menu that keeps showing until the user types "exit".
while True:
    print("\nMENU:")
    print("1. chapati")
    print("2. ugali")
    print("3. chicken")
    print("Type 'exit' to quit")

    choice = input("Enter your choice: ")

    if choice == "exit":
        print("Goodbye!")
        break
