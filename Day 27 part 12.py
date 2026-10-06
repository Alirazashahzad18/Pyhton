def count_numbers(start, end):
    for i in range(start, end + 1):
        yield i


my_generator = count_numbers(10, 15)

for number in my_generator:
    print(number)