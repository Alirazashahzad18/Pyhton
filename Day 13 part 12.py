with open ("student.txt", "r") as file:
    Total_students = 0
    longest = ""
    shortest = None
    A_names = 0
    total_character = 0

    for line in file:
      name = line.strip()
      total_character = total_character + len(name)
    
      Total_students= Total_students + 1
      if len(name) > len(longest):
         longest = name
      if shortest is None or len(shortest)> len(name):
         shortest= name
      if name.startswith("A"):
        A_names = A_names + 1

        
    
    print ("Total students:" , Total_students)
    print("Longest name:", longest)
    print("Shortest name:", shortest)
    print("Names starting with A:", A_names)
    print("Total charcters:", total_character)

        