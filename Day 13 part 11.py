with open ("student.txt", "r") as file:
    shortest = None
    for line in file:
        name = line.strip()
        if  shortest is None or len(shortest) > len(name):
            shortest = name
    print("shortest name= ", shortest)