try:
    number = int(input("Enter the number: "))
    print(number)
except ValueError:
    print("Invalid input! Please enter a number")