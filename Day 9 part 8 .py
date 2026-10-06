names = ["Ali", "Ahmed", "Usman", "Ayesha", "Umar", "Hamza"]
upper_names= []
for name in names:
    if name.startswith("A"):
        upper_names.append(name.upper())
print(upper_names)
