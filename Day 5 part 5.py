numbers = (12, 5, 18, 7, 25, 10, 30)

number = int(input("Enter number= "))

if number in numbers:
    print(str(number)+ " is in the tuple")
    print(numbers.index(number))
else:
    print(str(number)+ " is not in the tuple")