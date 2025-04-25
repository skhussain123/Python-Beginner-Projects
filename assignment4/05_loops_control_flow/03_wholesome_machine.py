affirmation = "I am capable of doing anything I put my mind to."

def main():
    
    while True:
        user_input = input("Please type the following affirmation: " + affirmation + " ")

        if user_input == affirmation:
            print("That's right! :)")
            break 
        else:
            print("Hmmm That was not the affirmation. Try again.")

if __name__ == "__main__":
    main()
