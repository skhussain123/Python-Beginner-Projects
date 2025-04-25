# Sample inventory dictionary
inventory = {
    "apple": 50,
    "banana": 30,
    "pear": 1000,
    "orange": 20
}

def num_in_stock(fruit):
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip()
    count = num_in_stock(fruit)

    if count > 0:
        print("This fruit is in stock! Here is how many:")
        print(count)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
