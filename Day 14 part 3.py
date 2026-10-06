try:
    number1 = int(input("Enter first num: "))
    number2 = int(input("Enter second num: "))
    result = number1 / number2
    print(result)
except ValueError:
    print("Invalid input! Please enter numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")