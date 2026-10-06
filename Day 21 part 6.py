marks = [85, 72, 91, 65]

result = any(mark>= 90 for mark in marks)
result2 = all(mark >= 40 for mark in marks)
print(result)
print(result2)