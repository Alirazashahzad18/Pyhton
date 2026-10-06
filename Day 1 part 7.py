name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age < 0:
    print("Invalid age. ")
elif age <= 12:
    print(name + " you are a child. ")
elif age <= 19:
    print(name + " you are a teenager.")
elif age <= 59:
    print(name + " you are an adult. ")
else:
    print(name + " you are a senior citizen ")