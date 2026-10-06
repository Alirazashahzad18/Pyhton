names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 65]

for index, (name, mark) in enumerate(zip(names, marks), start= 1):
    print(index, name, mark)