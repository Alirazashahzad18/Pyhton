with open ("student.txt", "r") as file:
    count = 0 
    for line in file:
        name = line.strip()

        if len(name)>= 4:
            count = count + 1
    print("Total count= " + str(count))