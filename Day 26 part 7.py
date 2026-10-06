students = ["Ali", "Ahmed", "Usman", "Hamza", "Ayesha"]

my_iterator = iter(students)

first = next(my_iterator)
second = next(my_iterator)

print("First:", first)
print("Second:", second)

for name in my_iterator:
    print("Remaining:", name)