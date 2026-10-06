def student_info(*marks, **info):
    print(info)

    total = 0

    for mark in marks:
        total = total + mark
        print(mark)

    len_marks = len(marks)
    average = total / len_marks

    print("Total:", total)
    print("Average:", average)


student_info(
    85, 90, 78,
    name="Ali",
    age=22
)