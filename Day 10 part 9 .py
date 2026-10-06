names = ["Ali", "Ahmed", "Usman", "Ayesha", "Umar", "Hamza"]
uppercase= [name.upper() for name in names if name.startswith("A") and len(name) >= 5]

print(uppercase)