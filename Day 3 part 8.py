def number_checker(num):
    if num ==0:
        return "zero"
    elif num < 0:
        return "negative"
    elif num % 2 ==0:
        return "positive even"
    else:
        return "positive odd"

number= int(input("Please enter your number: "))

result= number_checker(number)
print("the number is: ", result)
    