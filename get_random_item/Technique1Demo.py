"""
LESSON: 4.1 - Lists
TECHNIQUE 1: Get Random Item
DEMO
"""

# --- Setup --- #
import random
animals = ["lion", "horse", "dog", "bird", "human", "bat", "cat", "goat"]

# --- Get random parts --- #
randhead = random.randint(0, len(animals)-1)
head = animals[randhead]
randbody = random.randint(0, len(animals)-1)
body = animals[randbody]

head = random.choice(animals)
body = random.choice(animals)
# --- Print --- #
print("The " + head + body + " is a mythical creature.")
print("It has the head of a " + head + " and the body of a " + body + ".")

