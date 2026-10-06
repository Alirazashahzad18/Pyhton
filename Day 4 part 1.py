programming_languages= ['Python','Java','C++','Node.js','C#']

print(programming_languages)
print(programming_languages[0])
print(programming_languages[2])

programming_languages[1] = 'Javascript'
programming_languages[4] = 'C'

print(programming_languages)

programming_languages.append('PHP')
programming_languages.append('Go')

print(programming_languages)

programming_languages.remove('PHP')
programming_languages.remove(programming_languages[2])

print(programming_languages)

Total_languages = len(programming_languages)
print("total number of programming languages in the list is= ", Total_languages)