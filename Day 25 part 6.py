students = {
    "Ali": 85,
    "Ahmed": 42,
    "Usman": 91,
    "Hamza": 35,
    "Ayesha": 68,
    "Zain": 82,
    "Noor": 91,
    "Sara": 85
}

result= sorted(
    filter(
        lambda item: item[1] >= 60,
        students.items()
    ),
    key = lambda item:
    ("A" if item[1] >= 80
    else "B"
    if item[1] >= 60
    else "C"
    if item[1] >= 40
    else "F",
    -item[1], len(item[0]),item[0] 
    )
)

name = [item[0] for item in result]

print(name)