def count_numbers():
    for i in range(1, 11):
        yield i
     

my_generator = count_numbers()

for number in my_generator:
    print(number)