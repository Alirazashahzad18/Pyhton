try:
    number = int(input("Enter the number: "))

except ValueError:
    print("Invalid input!")

else:
    print("Valid number:", number)