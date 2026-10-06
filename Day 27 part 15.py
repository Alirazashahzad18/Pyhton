def excellent_students(students):
    for name, mark in students.items():
        if mark >= 80:
            yield name,mark

students = {
    "Ali": 75,
    "Ahmed": 88,
    "Usman": 92,
    "Hamza": 45,
    "Ayesha": 81,
    "Zain": 67
}

my_generator = excellent_students(students)

for name,mark in my_generator:
    print(name,mark)