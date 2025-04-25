# Initialize an empty phonebook dictionary
phonebook = {}

def add_contact(name, phone_number):
    """Add a contact to the phonebook."""
    phonebook[name] = phone_number
    print(f"Contact {name} added with phone number {phone_number}.")

def search_contact(name):
    """Search for a contact in the phonebook."""
    if name in phonebook:
        print(f"Phone number for {name}: {phonebook[name]}")
    else:
        print(f"Contact {name} not found in the phonebook.")

def display_phonebook():
    """Display all contacts in the phonebook."""
    if phonebook:
        print("Phonebook contents:")
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")
    else:
        print("Phonebook is empty.")

def main():
    """Main function to interact with the phonebook."""
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Phonebook")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the phone number: ")
            add_contact(name, phone_number)
        elif choice == '2':
            name = input("Enter the name to search: ")
            search_contact(name)
        elif choice == '3':
            display_phonebook()
        elif choice == '4':
            print("Exiting phonebook...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
