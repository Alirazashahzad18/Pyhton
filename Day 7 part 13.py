python_students = {"Ali", "Ahmed", "Usman", "Hamza"}
java_students = {"Ahmed", "Hamza", "Bilal", "Zain"}

total_student= python_students.intersection(java_students)
only_python_students= python_students.difference(java_students)
enrolled_in_one_subject_students= python_students.symmetric_difference(java_students)

print(total_student)
print(only_python_students)
print(enrolled_in_one_subject_students)