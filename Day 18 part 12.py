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
    key=lambda items: (
        0 if items[1] >= 90 else
        1 if items[1] >= 80 else
        2 if items[1] >= 70 else
        3 if items[1] >= 60 else
        4 if items[1] >= 50 else
        5 if items[1] >= 40 else
        6 if items[1] >= 30 else
        7 if items[1] >= 20 else
        8 if items[1] >= 10 else
        9,
        items[1]
    )
)

print(result)