def square():
    for i in range(1, 11):
        yield i * i

my_generator = square()

for number in my_generator:
    print(number)
