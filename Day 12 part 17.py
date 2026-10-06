with open ("Student.txt", "r") as file:
    student_name = input("Enter the Name: ")
    found = False

    for line in file:
        if student_name.lower() in line.lower():
            student_found = line.strip()
            found = True

    if found:
        print("Student found: " + student_found)
    else:
        print("Student not found!")