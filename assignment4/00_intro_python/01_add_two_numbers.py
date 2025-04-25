# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

print("This program adds two numbers.")

try:
    firstnum: str = input("Enter first Number: ")
    first = int(firstnum)

    secnum: str = input("Enter Second Number: ")
    sec = int(secnum)

    total = first + sec
    print("The total is:", total)

except ValueError:
    print("Error: Please enter valid integer numbers.")
