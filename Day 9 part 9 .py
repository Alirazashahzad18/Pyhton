students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}
passed_students= []
for name, marks in students.items():
    if marks >= 70:
        passed_students.append((name, marks))
print(passed_students)