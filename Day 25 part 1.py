students = {
    "Ali": 85,
    "Ahmed": 42,
    "Usman": 91,
    "Hamza": 35,
    "Ayesha": 68,
    "Zain": 82
}

result = sorted(
    students.items(),
    key = lambda item: 
    "A" if item[1] >= 80
    else "B" 
    if item[1] >= 60
    else "C"
    if item[1] >= 40
    else "F"
)

print(result)