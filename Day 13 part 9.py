with open ("student.txt", "r") as file:
    total_vowels = 0
    for line in file:
        name= line.strip()
        for character in name.lower():
            if character in "aeiou":
                total_vowels = total_vowels + 1
    print("Total vowels: ", total_vowels)