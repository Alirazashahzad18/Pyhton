with open ("student.txt", "r") as file:
    student_name = input("Please enter the name: ")

    found = False

    for line in file:
        if student_name in line:
            found = True

    if found :
        print("Student found!")
    else :
        print("Student not found!")