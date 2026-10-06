def calculator (number1,number2,operator):
    if operator == "+":
        return number1+number2
    elif operator == "-":
        return number1-number2
    elif operator == "*":
        return number1*number2
    elif operator == "/" and number2 == 0:
        return " Division by zero is not allowed."
    elif operator == "/":
        return number1/number2
    else:
        return "Invalid operator"

number1= int(input("Please Enter the first number: "))
number2= int(input("Please Enter the second number: "))
operator= input("Please Enter the operator: ")

result= calculator(number1,number2,operator)
print("The result of the operation is: ", result)

