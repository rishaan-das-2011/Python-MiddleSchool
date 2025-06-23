"""
LESSON: 4.2 - For Each
TECHNIQUE 2: Count Items
DEMO
"""

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

# Count the numbers with three letters
three_letters = 0
for num in numbers:
    if len(num) == 3:
        three_letters += 1



print(str(three_letters) + " of the numbers from 1 to 10 are written with three letters.")