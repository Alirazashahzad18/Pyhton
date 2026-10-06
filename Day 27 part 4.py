def numbers():
    yield 10
    yield 20
    yield 30
    yield 40

my_generator = numbers()

for number in my_generator:
    print(number)