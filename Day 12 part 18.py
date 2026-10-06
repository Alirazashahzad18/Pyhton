with open ("student.txt", "r") as file:
    student_name = input("Please enter the name of the student: ")
    count =  0

    for line in file:
        if student_name.lower() in line.lower():
            count = count + 1

    if count:
        print("Found " + str(count) + " student")
    else:
        print("Found 0 students")