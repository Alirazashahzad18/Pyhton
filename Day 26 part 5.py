names = ["Ali", "Ahmed", "Usman"]

my_iterator = iter(names)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

my_iterator = iter(names)

print("Again:")

print(next(my_iterator))
print(next(my_iterator))