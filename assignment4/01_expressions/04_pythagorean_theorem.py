import math

# Get the two side lengths from the user and cast them to be numbers
ab: float = float(input("Enter the length of AB: "))
ac: float = float(input("Enter the length of AC: "))

# Calculate the hypotenuse using the Pythagorean theorem
bc: float = math.sqrt(ab**2 + ac**2)

# Print the result
print("The length of BC (the hypotenuse) is: " + str(bc))
