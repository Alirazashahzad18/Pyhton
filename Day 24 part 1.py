students = {
    "Ali": 85,
    "Ahmed": 91,
    "Usman": 85,
    "Ayesha": 91,
    "Hamza": 72
}

result = sorted(
    students.items(),
    key = lambda item: (item[1], item[0])
)

print(result)