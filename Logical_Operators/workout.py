# challenge 
age = int(input("Enter your age"))
grade = float(input("Enter you grade"))

if age >= 18 and grade >=50:
    print("Eligible for scholorship")
else:
    if age < 18 and grade < 60:
        print("not old enough and grade not high enough")
    elif age < 18:
        print("not old enough  ")
    elif grade < 60:
        print("grade not hight enough")
