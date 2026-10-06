names = ["Ali", "Ahmed", "Usman", "Hamza"]
marks = [85, 72, 91, 35]

result = all(  mark >=  40  for mark in marks)
print(result)