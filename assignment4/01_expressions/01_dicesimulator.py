import random

def roll_dice():
    return random.randint(1, 6)

# Simulate rolling two dice three times
for i in range(1, 4):
    die1 = roll_dice()
    die2 = roll_dice()
    print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")
