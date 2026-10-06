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
    total = total + student[name]["marks"]

average = total/ len(student)

for name in student:
    if student[name]["marks"] > average:
        print(name, "-", student[name]["marks"])