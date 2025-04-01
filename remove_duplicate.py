numbers = [1, 2, 2, 3, 4, 4, 5]

# Method 1: Using set()
unique_numbers = list(set(numbers))
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

# Method 2: Using loop
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)  # Output: [1, 2, 3, 4, 5]
