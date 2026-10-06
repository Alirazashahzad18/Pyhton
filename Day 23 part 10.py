students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Ayesha": 88,
    "Noor": 95
}

result = sorted(
    filter(
        lambda item: item[1] >= 80
        and
        len(item[0]) >= 4,
        students.items()
    ),
    key= lambda item: item[1],
    reverse = True
)
names = [ item[0] for item in result]
print(names)