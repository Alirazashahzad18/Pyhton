students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Ayesha": 88
}

shortest_name= min(
    students.items(),
    key = lambda item: len(item[0])
    )
print(shortest_name)