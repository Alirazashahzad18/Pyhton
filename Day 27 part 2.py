def numbers():
    yield 10
    yield 20
    yield 30

my_generator = numbers()

print(type(my_generator))