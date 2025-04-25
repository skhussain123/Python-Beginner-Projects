def main():
    values = [] 
    
    while True:
        value = input("Enter a value: ")
        if value == "": 
            break
        values.append(value)
    
    print("Here's the list:", values) 

if __name__ == "__main__":
    main()
