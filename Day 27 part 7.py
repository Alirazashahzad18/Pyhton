def even_numbers():
    for i in range(1, 21):
        if i % 2 ==0:
            yield i


my_generator = even_numbers()

for number in my_generator:
    print(number)