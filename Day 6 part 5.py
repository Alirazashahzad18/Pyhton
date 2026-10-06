student= {
    "name": "Ali",
    "age": 22,
    "city": "Islamabad",
    "university": "UMT",
    "Semester": 6
}
total=0
count=0
for key,value in student.items():
    if type(value) == int:
        total=total+value 
        count=count+1
        average=total/count
print(average)