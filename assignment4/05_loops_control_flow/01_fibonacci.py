MAX_VALUE = 10000

def fibonacci_sequence():

    a, b = 0, 1
    print(a, end=" ")
    
    while b < MAX_VALUE:
        print(b, end=" ")
        a, b = b, a + b  

fibonacci_sequence()
