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


# challenges 2 Discount with membership or coupon 

original_price = 1000
has_membership = True
has_coupon = "valid"

if has_membership or has_coupon == "valid":
    discount = 0.10
    final_price = original_price *(1- discount)
    print("discoutn applied")
else:
    final_price = original_price
    print("No discount")

print(f"final price: {final_price:.2f}")


# challenge 3 check weekend 

day = input("Enter a day of the week (e.g, Monday)").title()

if not (day == "Saturday" or day == "Sunday"):
    print("It's a weekday")
else:
    print("It's weekend")


# challenge 4 checking username and password

currect_username = "user123"

username = input("enter username")
password = input("Enter password")

if username == currect_username and password != "":
    print("Loging Succefuly")

elif username != currect_username and password == "":
    print("username and password is incorrect")
else:
    if username != currect_username:
        print("user name is wrong")
    elif password == "":
        print("password is wrong")
    