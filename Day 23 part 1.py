students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Ayesha": 88
}

result = sorted(
    students.items(),
    key = lambda item: item[1]
)

print(result)