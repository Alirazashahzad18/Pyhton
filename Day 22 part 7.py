students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Ayesha": 88
}

longest_name = max(
    students.items(),
    key = lambda item: len(item[0])
)
print(longest_name[0])