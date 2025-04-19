
print(True and False)

print(False or True)

print(not False)

print(5 > 3 and 2 < 1)

print(10 != 5 or 3 == 3)

a = 10 
b = 5
c = 0

print(a > b and b > c)

print(a < b or c == 0)

print(not (a == 10))


# you need to make the expressions evaluate to True

#1 Replace ___ with th correct value

print(5 > 3 and 3 < 10)

print(not (10 == 5))

print((3<4) or (3>6),"print ture i think")


# Real life scenario : login logic

username = "admin"
password = "1234"

# Simulate logic
input_user = input("Username: ")
input_pass = input("Password: ")

if input_user == username and input_pass == password:
    print("Login successful")

else:
    print("Access Denied")