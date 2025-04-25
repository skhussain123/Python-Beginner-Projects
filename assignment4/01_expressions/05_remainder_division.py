# Get input from the user
firstvalue: int = int(input("Please enter an integer to be divided: "))
secondvalue: int = int(input("Please enter an integer to divide by: "))

# Perform integer division and get the remainder
quotient: int = firstvalue // secondvalue
remainder: int = firstvalue % secondvalue

# Display the result
print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
