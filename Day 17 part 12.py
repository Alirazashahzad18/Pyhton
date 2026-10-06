names = ["Ali", "Ahmed", "Usman", "Ayesha", "Hamza", "Asad"]

start_with_a = lambda name: name.startswith("A")

result = list(filter(start_with_a, names))
print(result)