students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}

result= sorted(filter (lambda items: items[1] >= 80, students.items()), key = lambda items: items[1], reverse = True)
print(result)