name = input("Please enter your name: ")
marks = int(input("Please enter your marks: "))

print(name + ", your marks are " + str(marks) + ".")

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Your result is excellent.")
elif marks >= 80:
    print("Your result is very good.")
elif marks >= 70:
    print("Your result is good.")
elif marks >= 60:
    print("You are passed.")
else:
    print("Fail.")