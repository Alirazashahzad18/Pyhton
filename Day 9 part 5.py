numbers= [10, 15, 22, 7, 30, 41, 18, 25]
even_numbers= []
for number in numbers:
    if number %2 == 0:
        even_numbers.append(number)
print(even_numbers)