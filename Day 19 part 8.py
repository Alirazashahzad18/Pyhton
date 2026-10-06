students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 35,
    "Ayesha": 88
}

passing_students = filter(lambda items: items[1] >= 40, students.items())
for index, (name, mark) in enumerate(passing_students, start= 1):
    print(index, name, mark)
