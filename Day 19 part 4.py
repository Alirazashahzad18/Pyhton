names = ["Ali", "Ahmed", "Usman", "Hamza", "Ayesha"]

for index, name in enumerate(names, start= 1):
    if name.startswith("A"):
        print(index, name)