"""
LESSON: 4.2 - For Each
INSTRUCTION 1
"""

# Setup
import random
fav_foods = ["french fries", "veggie lo mein", "fried cauliflower", "mashed potatoes"]

# Get random choice
choice = random.randint(0, len(fav_foods) - 1)

for food in fav_foods:
    print("Do you like " + food + "?")

# User input
    answer = input("y/n: ")
    if answer == "y":
            print("Do you like " + food + "?")
            print("You have good taste!")
    