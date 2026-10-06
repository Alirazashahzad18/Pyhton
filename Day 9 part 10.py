students = {
    "Ali": 85,
    "Ahmed": 72,
    "Usman": 91,
    "Hamza": 65,
    "Ayesha": 88
}
good_students= []
total= 0
count= 0
for name , marks in students.items():
    total= total + marks
    count= count + 1
average= total/ count
print(average)
for name, marks in students.items():
    if marks > average:
        good_students.append(name)
print(good_students)