students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65
}

highest_marks= max(
    students.items(),
    key= lambda item: item[1]
 )
print(highest_marks)