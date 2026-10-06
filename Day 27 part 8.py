marks = [45, 72, 91, 38, 85, 60, 33, 78]

def passing_marks():
    for mark in marks:
        if mark >= 50:
            yield mark


my_generator = passing_marks()

for mark in my_generator:
    print(mark)