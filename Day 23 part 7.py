students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Ayesha": 88
}

result = sorted(
    filter(
        lambda item: item[1] >= 80
        and
        len(item[0]) >= 4,
        students.items()
    ),
    key = lambda item: item[1],
    reverse= True
)
print(result)