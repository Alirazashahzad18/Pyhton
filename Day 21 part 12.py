names = ["Ali", "Ahmed", "Usman"]
marks = [85, 72, 91]

result = all(
    mark >= 60 
    for name, mark in zip(names, marks)
)

print(result)