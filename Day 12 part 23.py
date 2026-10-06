with open ("student.txt", "r") as file:
    longestname = ""

    for line in file:
        name = line.strip()
        if len(name) > len(longestname):
            longestname = name
    print("Longest student name= " + longestname)