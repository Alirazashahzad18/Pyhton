numbers= [10, 15, 22, 7, 30, 41, 18, 25]
large_numbers= []

for number in numbers:
    if number %2 == 0 and number > 20:
        large_numbers.append(number)
print(large_numbers)