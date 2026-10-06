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

highest = 0
top_student = ""

for name in student:
    if student[name]["marks"] > highest:
        highest = student[name]["marks"]
        top_student = name

print("Top student:", top_student)
print("Marks:", highest)