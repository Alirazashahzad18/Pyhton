marks = [45, 72, 91, 38, 85, 60, 33, 78, 95, 41]

def passed_marks():
    for mark in marks:
        if mark >= 50:
            bonus = mark + 5

            if mark >= 100:
                bonus = 100

            yield bonus


my_generator = passed_marks()

for mark in my_generator:
    print(mark)