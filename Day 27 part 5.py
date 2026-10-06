def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


my_generator = count_numbers()

for number in my_generator:
    print(number)