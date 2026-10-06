students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Ayesha": 88
}

highest_mark_student = max(
    students.items(),
    key = lambda item: item[1]
)
print(highest_mark_student[0])