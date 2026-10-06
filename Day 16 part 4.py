def count_positive(*numbers):


    count = 0
    for number in numbers:
        if number > 0:
            count = count + 1
    return count

result = count_positive(10,-5,20,-2,0,15)
print (result)