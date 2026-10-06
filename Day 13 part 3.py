with open("student.txt", "r") as file:
    for line in file:
        name = line.strip()

        print(name.upper())