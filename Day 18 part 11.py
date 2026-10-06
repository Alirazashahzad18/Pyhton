students = {
    "Ali": 85,
    "Ahmed": 42,
    "Usman": 91,
    "Hamza": 35,
    "Ayesha": 68
}

result = sorted(students.items(), key = lambda items: 0 if items[1] >= 80 else 1 if items[1] >= 60 else 2 if items[1] >= 40 else 3)

print(result)