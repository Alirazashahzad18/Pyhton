names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 65]

for name , mark in zip(names, marks):
    if mark >= 80:
        print(name, mark)