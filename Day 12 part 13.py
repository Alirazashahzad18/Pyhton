with open ("student.txt", "w") as file:
    student1 = input("Please enter the name of student 1: ")
    student2 = input("Please enter the name of student 2: ")
    student3 = input("Please enter the name of student 3: ")

    students= [student1, student2, student3]
    for student in students:
        file.write(student + "\n")