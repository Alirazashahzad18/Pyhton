programming_languages= ['Python','Javascript','C++','Go','Ruby']

language= input("Please enter the language that you want to check= ")
if language in programming_languages:
    print(language +" is in the list")
else:
    print(language +" is not in the list")