def top_students(students):
    for name, mark in students.items():
        if mark >= 80:
            yield name,mark

students = {
    "Ali": 85,
    "Ahmed": 42,
    "Usman": 91,
    "Hamza": 35,
    "Ayesha": 68,
    "Zain": 82,
    "Noor": 95
}

my_generator = top_students(students)

for name, mark in my_generator:
    print(name, mark)