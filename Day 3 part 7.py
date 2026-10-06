def check_number(num):

    if num == 0:
        return "Zero"

    elif num < 0:
        return "Negative"

    elif num % 2 == 0:
        return "Positive even"

    else:
        return "Positive odd"


number = int(input("Please enter the number: "))

result = check_number(number)

print("The number is:", result)