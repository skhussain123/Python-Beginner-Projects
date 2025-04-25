import random

DONE_LIKELIHOOD = 0.3

def done():
    """Randomly returns True or False based on DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Counts from 1 to 10, stops if done() returns True."""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    
    for i in range(1, 11):
        if done(): 
            print()
            return 
        print(i, end=" ") 

def main():
    chaotic_counting()
    print("I'm done.")


if __name__ == "__main__":
    main()
