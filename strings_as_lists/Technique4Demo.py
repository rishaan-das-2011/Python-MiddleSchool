"""
LESSON: 4.1 - Lists
TECHNIQUE 4: Strings as Lists
DEMO
"""

sentence = input("Please type a sentence: ")
output = ""

# Go through the string and build a new one
index = 0
while index < len(sentence):
    if sentence[index] == "a":
        output += "o"
    else:
        output += sentence[index]
    index += 1


print("Here is your transformed sentence:")
print(output)