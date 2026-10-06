student = {
    "Ali": {
        "age": 22,
        "marks": 85
    },
    "Ahmed": {
        "age": 21,
        "marks": 72
    },
    "Usman": {
        "age": 23,
        "marks": 91
    }
}

total = 0
for name in student:
    total += student[name]["marks"]

average = total / len(student)
print("Average: ", average)