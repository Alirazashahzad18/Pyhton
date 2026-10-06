students = {
    "Ali": 85,
    "Ahmed": 91,
    "Usman": 85,
    "Hamza": 91,
    "Ayesha": 88
}

result = sorted(
    students.items(),
    key=lambda items: (-items[1], items[0])
)
print(result)