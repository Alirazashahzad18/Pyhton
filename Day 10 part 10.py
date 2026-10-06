students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}
average = sum(students.values()) / len(students)
names=[name.upper() for name, mark in students.items() if mark>= average]
print(names)