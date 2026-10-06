value= input("Enter something= ")

if value.isdigit():
    print("It is number")
elif value.isalpha():
    print("It is text")
else:
    print("It contains numbers and letters")