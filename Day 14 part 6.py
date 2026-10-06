try:
    name = input("Enter name: ")
    marks = int(input("Please enter marks:"))
except:
    print("Invalid input!")
else:
    if marks >= 80:
        print("Grade: Excellent")
    elif 60 <= marks >= 79:
        print("Grade: Good")
    elif 40 <= marks >= 59:\
        print("Grade: Pass")
    else:
        print("Grade: Fail")
finally:
    print("Program Finished.")