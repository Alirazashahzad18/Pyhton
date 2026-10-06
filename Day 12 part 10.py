with open("student.txt", "w") as file:
    name= input("Please enter your name: ")
    age= input("Please enter your age: ")
    file.write("Name: "+ name)
    file.write("\nAge: "+ age)