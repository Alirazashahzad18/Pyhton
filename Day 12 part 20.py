with open ("student.txt", "r") as file:

    count = 0
    print ("Students: ")
    for line in file:
        count= count + 1
        print(line.strip())

    print("Total students: " + str(count))
    