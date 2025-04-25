def count_even(lst):

    even_count = 0
    for num in lst:
        if num % 2 == 0: 
            even_count += 1
    
    print(f"There are {even_count} even numbers in the list.")

def get_input():

    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  
        lst.append(int(user_input))
    
    return lst

def main():

    lst = get_input()
    count_even(lst)

if __name__ == "__main__":
    main()
