student= {
    "name": "Ali",
    "age": 22,
    "city": "Lahore",
    "university": "UMt"
}

print(student["name"])
print(student["age"])
print(student["city"])

student["city"] = "Islamabad"

print(student["city"])
student["semester"]= 6
print(student["semester"])
print(student)

student["course"]= "python"

print(student)

del student["course"]

print(student)

print(len(student))