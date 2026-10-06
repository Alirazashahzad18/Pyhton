def smallest_num(*numbers):

    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

result = smallest_num(25,10,40,5,18)

print(result)