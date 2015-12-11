from pip._vendor.distlib.compat import raw_input
def factorialRecursion(number):
    
    if number <= 1:
        return 1
    else:
        return number * factorialRecursion(number - 1)
    
print("Enter a number: ")
usernumber = int(raw_input())
print(str(usernumber) + "!: " + str(factorialRecursion(usernumber)))
