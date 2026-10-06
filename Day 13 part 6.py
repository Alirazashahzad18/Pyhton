with open ("student.txt", "r") as file:
    number = 1
    for line in file:
        name = line.strip()
        
        print(number,".",name )
        number = number + 1