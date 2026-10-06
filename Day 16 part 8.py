def student_info(*marks, **info):

    print(info)

    for mark in marks:
        print(mark)


student_info(
    85, 90, 78,
    name="Ali",
    age=22
)