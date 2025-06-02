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