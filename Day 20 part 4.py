names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 65]
cities = ["Lahore", "Islamabad", "Karachi", "Multan"]

for name, mark, city in zip(names, marks, cities):
    print(name, mark, city)