with open("students.txt", "w") as file:

    student1 = input("Enter student 1: ")
    student2 = input("Enter student 2: ")
    student3 = input("Enter student 3: ")

    students = [student1, student2, student3]

    for student in students:
        file.write(student + "\n")