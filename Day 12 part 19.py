with open ("student.txt", "a") as file:
    student_name = input("Please enter the student name: ")
    file.write(student_name + "\n")