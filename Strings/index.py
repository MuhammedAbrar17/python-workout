strings = "Your defenses are just delays."
print(strings)

strings1 = """We are Anonymous. We are Legion. 
We do not forgive. We do not forget. Expect us."""
print(strings1)

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated_string = str1 + ", " + str2
print(concatenated_string)  # Hello, World

# str. upper() & str.title()

phrase = "i am python django react developer"
cap_phrase = phrase.capitalize()

title_pharse  = phrase.title()
print(cap_phrase)
print("title_phrase =", title_pharse)


# str.strip(), str.lstrip(),and str.rstrip() (its remove spaces on the value)
title = "   hello   hay    "
print(title.strip()) # its remve all spaces (left and right) on the sentence

print(title.lstrip())# its remove left side space only

print(title.rstrip())# its remve right side space only


# str.startwith(prefix) and str.endswith(suffix)
filename = "Muhammed Abrar"
start_with = filename.startswith('Muham')
print(start_with)
end_with = filename.endswith("abu")
print(end_with)

# str.replace(old,new)

name = "abu abrar"
replaced_name = name.replace("abu","muhammed")
print(replaced_name)

# str.find() and str.index()

phrase1 = "Hey i become an ethical hacker on 2025 end"
find = phrase1.find("hacker")
find2 = phrase1.index("ethical")
print(find,find2)


#str.split(separator)
sentence = "Abu is a dengours hacker in the world"
word = sentence.split()
print(word)

# str.count(substring)
senten = "python is very funny. python is easy . python is very powerfull"
count = senten.count("python")
print(count)