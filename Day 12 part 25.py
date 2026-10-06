with open ("student.txt", "r") as file:
    student = []
    longest= "" 
    shortest = None
    a_count = 0
    total_characters = 0

    for line in file:
        name = line.strip()
        