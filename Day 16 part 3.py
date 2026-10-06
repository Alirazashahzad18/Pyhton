def find_largest(*numbers):

    largest = 0
    for number in numbers:
        if number > largest:
            largest = number

    return largest

result = find_largest(10,45,23,78,12)
print(result)
