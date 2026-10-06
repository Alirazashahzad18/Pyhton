def add_even_numbers(*numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total = total + number
    return total

result = add_even_numbers(10,15,20,25,30)
print (result)
         


