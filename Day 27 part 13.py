def even_number(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i

my_generator = even_number(1, 20)

for number in my_generator:
    print(number)