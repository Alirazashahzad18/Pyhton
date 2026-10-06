names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 65]
cities = ["Lahore", "Islamabad", "Karachi", "Multan"]

for name, mark, city in zip (names, marks, cities):
    if mark >= 80:
        print(name, mark, city)