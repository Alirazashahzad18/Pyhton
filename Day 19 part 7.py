students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}

for index, (name,mark) in enumerate(students.items(), start = 1):
    if mark >= 80:
        grade= "A"
    elif mark >= 60:
        grade= "B"
    elif mark >= 40:
        grade= "C"
    else:
        grade= "F"
    print(index, name, mark,grade)