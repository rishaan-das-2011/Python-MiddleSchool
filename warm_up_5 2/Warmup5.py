"""
LESSON: 6.2 - Return Values
WARMUP 5
"""

import random

#### ------------------------------ ####
#### ---- GET LETTERS FUNCTION ---- ####
#### ------------------------------ ####
def get_letters(word_list, test_letter):

    total = 0

    for word in word_list:
        for letter in word:
            if letter == test_letter:
                total += 1

    # Return the calculated value

    return total


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
words = []

print("Enter 10 words. ")
while len(words) < 10:
    words.append(input("Enter word: "))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = random.choice(letters)

# Call the function and print the result
print("The letter: " + letter + " appeared " + str(get_letters(words, letters)) + " times.")