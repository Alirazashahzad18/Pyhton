with open ("student.txt", "r") as file:
    longest = "" 
    for line in file:
        name = line.strip()
        if len(name) > len(longest):
            longest = name 
    print("longest name: ", longest)