number = [10, 15, 20, 25, 30, 35, 40]

check = lambda number: number % 2 == 0

result = list(filter(check, number))

print(result)