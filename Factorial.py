from pip._vendor.distlib.compat import raw_input
print("Enter a number: ")
num = int(raw_input())
factorial = 1
for i in range(1, num+1):
   
    factorial = factorial * i
      
print(str(num) + "! = " + str(factorial))
