#string lenght
text = "Hello World"
print(len(text))

# Access charector 

text_1 = "Hey I am Abuzzyy"
print(text_1[0])
print(text_1[-1])


# Slicing 
text_2 = "Python"
print(text_2[0:4])
print(text_2[2:])
print(text_2[:4])

# String Methodes 
name = "muhammed abrar"
print(name.title()) # Muhammed Abrar
print(name.upper()) # MUAHMMED ABRAR
print(name.capitalize()) # Muhammed abrar
print(name.replace("abrar", "abu")) #muhammed abu


#Loop Through Character
Text = "Hello"
for char in Text:
    print(char)

# Count Vowels
sentence = "This is a simple sentence"
vowels = "aeiou"
count = 0
vowels_count = {}
for i in sentence.lower():
    if i in vowels:
        count += 1 
        if i in vowels_count:
            vowels_count[i] += 1
        else:
            vowels_count[i] = 1
        
print("total vowel count",count)
print("individuel vowel count")

for vowel,cnt in vowels_count.items():
    print(f"{vowel}:{cnt}")

# reverse string
text_3 = "PYTHON"
reversed_string = text[::-1]
print(reversed_string)

