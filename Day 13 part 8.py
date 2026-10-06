with open ("student.txt", "r") as file:
    total = 0
    for line in file:
        name= line.strip()
        total = total + len(name)
    print("Total Character: ", total)