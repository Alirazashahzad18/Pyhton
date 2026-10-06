def student_info(*marks, **info):
    print("Name:", info["name"],"\nAge:", info["age"])

    count = 0
    for mark in marks:
        if mark >= 40:
            count = count + 1
    print("Passing mark:", count)

student_info(
    85, 35, 90, 42, 28,
    name="Ali",
    age=22
)