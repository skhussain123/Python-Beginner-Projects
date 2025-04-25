def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    num = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(num, low, high):
        print(f"{num} is between {low} and {high}.")
    else:
        print(f"{num} is NOT between {low} and {high}.")

if __name__ == "__main__":
    main()
