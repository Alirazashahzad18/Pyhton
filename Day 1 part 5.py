name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
marks = int(input("Please enter your marks: "))

if age >= 18:
    print(name + " you are an adult.")
else:
    print(name + " you are a minor.")

if marks >= 80:
    print(name + " your grade is A.")
elif marks >= 70:
    print(name + " your grade is B.")
elif marks >= 60:
    print(name + " your grade is C.")
else:
    print(name + " you need to improve.")