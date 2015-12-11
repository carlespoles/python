def fibonacciRec(number):
    a = 1
    numberList = []
    numberList.append(a)
    while a < number:
        
        if a == 1:
            numberList.append(1)
        else:
            numberList.append(a)
            
        a = a + numberList[-2]
       
    return numberList

print(fibonacciRec(10))
