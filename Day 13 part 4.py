with open ("student.txt", "r") as file:
    with open ("upper_students.txt", "w") as output:
        for line in file:
            name = line.strip()
            output.write(name.upper()+ "\n")