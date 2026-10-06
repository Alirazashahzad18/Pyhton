students = {
    "Ali": 85,
    "Ahmed": 91,
    "Usman": 85,
    "Ayesha": 91,
    "Hamza": 72,
    "Noor": 72,
    "Zain": 85,
    "Sara": 91
}

result= sorted(
    filter(
        lambda item: item[1] >= 70,
        students.items()
    ),
    key= lambda item: (-item[1], len(item[0]), item[0])
)

name = [item[0] for item in result]

print(name)