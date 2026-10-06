number = [10, 15, 20, 25, 30]

check= lambda number: "Even" if number % 2 == 0 else "Odd"
result= list(map(check, number))
print(result)