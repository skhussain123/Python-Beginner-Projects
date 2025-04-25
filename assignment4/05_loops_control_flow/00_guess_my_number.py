import random

def guess_my_number():
    number_to_guess = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99... Try to guess it!")
    
    while True:
     
        guess = int(input("Enter a guess: "))
        
        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break 

guess_my_number()
