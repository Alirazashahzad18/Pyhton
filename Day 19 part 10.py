students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 35,
    "Ayesha": 88
}

a_students = filter(
    lambda items: items[0].startswith("A") and items[1] >= 80,
    students.items()
)
for index, (name,mark) in enumerate(a_students, start = 1):
    print(index, name, mark)