def fibonacci():
    fibList = []
    a, b = 0, 1
    # Take input from the user.
    n = int(input("How many terms? "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        fibList.append(n)
    else:  
        while a < n:
            fibList.append(a)
            a, b = b, a+b
        # Removing 0 from the list.    
        fibList.remove(0)
    
    if len(fibList) != 0:
        print("Fibonacci sequence:")
        print(fibList)
    
# Calling the function to test it.
fibonacci()
