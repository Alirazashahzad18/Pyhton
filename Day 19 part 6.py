students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}

for index, (name,mark) in enumerate(students.items(), start = 1):
    if mark >= 80:
        print(index, name, mark)