students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65
}

lowest_marks = min(
    students.items(),
    key = lambda item: item[1]
    )

print(lowest_marks)