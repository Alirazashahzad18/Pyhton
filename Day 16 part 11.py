def student_info(*marks, **info):
    print("Name:", info["name"],"\nAge:", info["age"])

    total = 0
    count = 0
    highest = marks[0]
    for mark in marks:
        total = total + mark
        average = total / len(marks)
        if mark >= 40:
            count = count + 1
        if mark > highest:
            highest = mark

    print("Total marks:", total)
    print("Average marks:", average)
    print("Passing mark:", count)
    print("Highest marks:", highest)

    
student_info(
    85, 35, 90, 42, 28,
    name="Ali",
    age=22
)