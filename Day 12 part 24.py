with open ("Student.txt", "r") as file:
    shortest = None

    for line in file:
        name = line.strip()

        if shortest is None or len(name) < len(shortest):
            shortest = name
            print(shortest)