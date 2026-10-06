search = input("Enter student name: ")
found = False

with open("student.txt", "r") as file:
    for line in file:
        name = line.strip()

        if name == search:
            found = True
            break

if found:
    print("Student found")
else:
    print("Student not found")