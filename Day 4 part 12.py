numbers= [12,5,18,7,25,10,30]

number= int(input("Please enter the number: "))
if number in numbers:
    print(str(number)+ " is in the list")
    if number% 2 == 0:
        print("It is even")
    else:
        print("It is odd")
else:
    print(str(number)+ " is not in the list")

