students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}

result = sorted(students.items(), key= lambda items: items[1])
print(result)