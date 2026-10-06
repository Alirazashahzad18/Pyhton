with open("student.txt", "r") as file:
    for line in file:
        name = line.strip()

        if len(name) >= 4:
            print(name)