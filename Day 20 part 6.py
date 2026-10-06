names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 65]
cities = ["Lahore", "Islamabad", "Karachi", "Multan"]

passing_students = filter(lambda items: items[1] >= 70, zip(names, marks, cities))
for index, (name, mark , city) in enumerate(passing_students, start=1):
    print(index, name, mark, city)