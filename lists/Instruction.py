"""
LESSON: 4.1 - Lists
INSTRUCTION 1
"""

# Library
import random

# Variables
animal1 = "tiger"
animal2 = "dog"
animal3 = "lizard"
animal4 = "hedgehog"
animal5 = "ferret"
animals  = ["tiger", "dog", "lizard", "hedgehog", "ferret", "penguin"]
animals[0] = "cheetah"
print(animals)
# Get random choice
choice1 = random.randint(0, len(animals)-1)
choice2 = random.randint(0, len(animals)-1)
# Select animal
# if choice == 1:
#    pet = animal1
# elif choice == 2:
#    pet = animal2
# elif choice == 3:
#    pet = animal3
# elif choice == 4:
#    pet = animal4
# elif choice == 5:
#    pet = animal5
#
# Output
print("Your pet is a " + animals[choice1] + animals[choice2])
print("It has the head of a " + animals[choice1] + " and the body of a " + animals[choice2])