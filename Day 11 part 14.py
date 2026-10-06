import random

numbers= random.randint(1,10)

number= int(input("Please enter the number: "))
if number == numbers:
    print("You guessed it!")
elif number > numbers:
    print("Too high!")
else:
    print("Too low!")