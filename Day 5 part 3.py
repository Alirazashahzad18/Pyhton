numbers= (5,10,15,20,25,30)
total= 0
for number in numbers:
    if number % 2 == 0:
        total= total + number
print(total)