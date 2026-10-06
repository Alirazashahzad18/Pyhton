with open("student.txt", "r") as file:
    with open("a_students.txt", "w") as output:
        for line in file:
            name= line.strip()
            if name.startswith("A"):
                output.write(name+ "\n")