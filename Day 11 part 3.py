import math

number =  int(input("Please enter the number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(math.factorial(number))