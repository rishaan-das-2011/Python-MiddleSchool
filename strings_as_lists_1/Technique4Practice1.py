"""
LESSON: 4.1 - Lists
TECHNIQUE 4: Strings as Lists
PRACTICE 1
"""

acronym = ""

word = ""
while word != "done":
    word = input("Please enter a word: ")

    # Concatenate the first letter of the word to
    # the acronym (unless the word is "done")
    if word == "done":
        break
        
    else:
        acronym += word[0]


print("These words make the acronym:")
print(acronym)


# Turn in your Coding Exercise.
