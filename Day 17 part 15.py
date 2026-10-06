numbers = [5, 10, 15, 20, 25, 30]

even_numbers = lambda number: number % 2 ==0

result = list(filter(even_numbers, numbers))
double = lambda number: number*2
doubled_result = list(map(double, result))
print(doubled_result)