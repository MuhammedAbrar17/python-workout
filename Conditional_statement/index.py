num = int(input("Enter a number"))

if num % 2 == 0:
    print("The number is Even ")
else:
    print("The number is Odd")

# challenge 2 

grade = input(chr("Enter your Grade ")).upper()

if grade == 'A' or grade == 'B' or grade == 'C':
    print("passing grade")
else :
    print("falling grade")


# challenge 3

day = input("Enter a day of the week(eg : Monday)").capitalize

if day == "Saturday" or day == "Sunday":
    print("weekend")
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("weekday")
else:
    print("invalid day enterd")

x = 0

if x > 0:
    print("x is positive")
elif x > 0 :
    print("x is negative")
else:
    print("x is zero")