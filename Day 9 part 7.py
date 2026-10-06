names = ["Ali", "Ahmed", "Usman", "Ayesha", "Umar", "Hamza", "Asad"]

count=0
for name in names:
    if name.startswith("A") and len(name)> 4 :
        count= count + 1
print(count)
