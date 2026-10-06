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
lowest_mark_student = min(
    students.items(),
    key = lambda item: item[1]
)
longest_name_student = max(
    students.items(),
    key = lambda item: len(item[0])
)
print("Highest:", highest_mark_student[0])
print("Lowest:", lowest_mark_student[0])
print("Longest:", longest_name_student[0])
