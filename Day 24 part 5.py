students = {
    "Ali": 85,
    "Ahmed": 91,
    "Usman": 85,
    "Ayesha": 91,
    "Hamza": 72,
    "Noor": 72,
    "Zain": 85
}

result = sorted(
    filter(
        lambda item: item[1]>= 80,
        students.items()
    ),
    key= lambda item:(-item[1], len(item[0]), item[0])
)
print(result)