students = ["Ali", "Ahmed", "Usman", "Hamza"]

my_iterator = iter(students)

print(next(my_iterator))
print(next(my_iterator))

for name in my_iterator:
    print(name)