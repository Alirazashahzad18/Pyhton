names = ["Ali", "Ahmed", "Usman", "Hamza", "Ayesha", "Noor"]

result = sorted(names, key = lambda name: len(name), reverse = True)

print(result)