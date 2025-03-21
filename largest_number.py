numbers = [3, 1, 7, 9, 2]

# Method 1: Using max()
print(max(numbers))  # Output: 9

# Method 2: Using loop
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)  # Output: 9
