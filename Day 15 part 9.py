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
total_marks = 0
total_students = 0 
average = 0
above = []
for name in student:
    total_marks = total_marks + student[name]["marks"]
    total_students = total_students + 1
    if student[name]["marks"]> highest:
        highest = student[name]["marks"]
        top_student = name
average = total_marks / total_students

for name in student:
    if student[name]["marks"] > average:
        above.append(name)
print("Total students:", total_students)
print("Total marks:", total_marks)
print("Average:", average)
print("Top student:", top_student)
print("Top marks:", highest)
print("Above average:", above)