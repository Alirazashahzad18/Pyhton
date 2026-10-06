try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    print("Valid Input", number)
finally:
    print("Program finished")
