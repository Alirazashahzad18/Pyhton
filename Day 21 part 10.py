names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 35]

result = any(
    name == "Ali" and mark >= 80
    for name , mark in zip(names, marks)
)

print (result)