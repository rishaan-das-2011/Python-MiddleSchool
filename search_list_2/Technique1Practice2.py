"""
LESSON: 4.2 - For Each
TECHNIQUE 1: Search List
PRACTICE 2
"""

import random

# --- Build list --- #
numbers = []
while len(numbers) < 8:
    number = random.randint(-100, 100)
    numbers.append(number)
print("Here are some numbers: " + str(numbers))

# --- Print positives --- #
print("These are the positive ones:")

# Print each positive number
for number in numbers:
    if number > 0:  
        
        print(number)

# Turn in your Coding Exercise.
