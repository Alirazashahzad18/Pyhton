names = ["Ali", "Ahmed", "Usman", "Ayesha", "Umar"]
upper_names= [name.upper() for name in names if name.startswith("A")]

print(upper_names)