s = "Python"

# Method 1 : Using Slice
print(s[::-1])

# Method 2 : Using reversed() function
print("".join(reversed(s)))

# Method 3 : Using for loop
revesed = ""
for i in s:
    revesed = i + revesed
    print(revesed)