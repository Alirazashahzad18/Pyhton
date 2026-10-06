def add_numbers(*numbers):
    total = 0 

    for number in numbers:
        total = total + number
       
    return total
result =  add_numbers(10,20,30,40)
print(result)
