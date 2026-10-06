def passing_marks(marks):
    for mark in marks:
        if mark >= 50:
            yield mark

marks = [35, 60, 88, 42, 95, 30, 76]

my_generator = passing_marks(marks)

for mark in my_generator:
    print(mark)
