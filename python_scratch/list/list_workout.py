#  Creating Lists

my_list = [1,2,34,5]
mixed_list = [1,"hello",3.23,True]
nested_list = [1,[2,3],4]

# Accessing Element 
print(my_list[0],my_list[-1])
print(nested_list[1][0])

# Basic operations
print(len(my_list)) # length
print(3 in my_list) # membership
print([1,2] + [3,4]) # concatination
print([1] * 3) # Repetition

# Slicing

print(my_list[1:4],my_list[:3], my_list[::-1]) # last on is reverse

#updating values 
my_list[1] = 23

#Adding Element
my_list.append(10) # adding at end
my_list.insert(2,33) # add at postiong
my_list.extend([2,4,55]) # add multiple

# Removing Elements 
my_list.remove(3) # remove by value
my_list.pop() # remove by index

