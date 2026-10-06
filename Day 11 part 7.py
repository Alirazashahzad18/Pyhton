import math

number1= int(input("Enter the first number: "))
number2= int(input("enter the second number: "))

print(math.lcm(number1,number2))

print(math.gcd(number1,number2))
if math.gcd(number1,number2) > 1:
    print("Numbers have a common factor.")
else:
    print("Numbers are relatively prime.")    

