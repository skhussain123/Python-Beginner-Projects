# Define the dictionary of fruits and their prices
fruit_prices = {
    "apple": 1.5,
    "durian": 5.0,
    "jackfruit": 3.0,
    "kiwi": 2.0,
    "rambutan": 4.0,
    "mango": 2.5
}

def main():
    total_cost = 0
    
    for fruit, price in fruit_prices.items():

        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price

    print(f"Your total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
