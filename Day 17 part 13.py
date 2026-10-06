numbers = [-10, 5, -3, 8, 0, 12, -7]

positive= lambda number: number > 0 

result= list(filter(positive, numbers)) 

print(result)