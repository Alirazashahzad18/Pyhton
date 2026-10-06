names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 65]

result= any(mark >= 80 for mark in marks)
print(result)