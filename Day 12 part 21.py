with open("student.txt", "r") as file, open("backup.txt", "w") as backup:
    for line in file:
        backup.writelines(line)


