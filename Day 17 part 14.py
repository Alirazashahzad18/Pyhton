marks = [35, 80, 45, 90, 55, 30, 75]

passing_marks = lambda marks: marks >= 40

result = list(filter(passing_marks, marks))

print(result)