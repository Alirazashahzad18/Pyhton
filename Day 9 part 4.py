names= ["Ali", "Ahmad", "Usman", "Hamza", "Ayesha", "Umar"]
short_names= []

for name in names:
    if len(name) <= 4:
        short_names.append(name)
print(short_names)