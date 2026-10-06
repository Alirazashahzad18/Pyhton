numbers= [10,20,30,40,50]

number= int(input("Please enter the number: "))
if number in numbers:
    print(str(number) + " is in the list")
else:
    print(str(number) + " is not in the list")