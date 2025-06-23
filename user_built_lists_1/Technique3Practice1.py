"""
LESSON: 4.1 - Lists
TECHNIQUE 3: User-Built Lists
PRACTICE 1
"""

# --- Setup --- #
animals = []

# --- Enter animals --- #

# Until the user enters "done", get animals as input
# and add each one to the list of animals

while True:
    animal = input("Enter an animal (type done to exit)")
    if animal == "done" or animal == "Done" or animal == "DONE":
        break
    animals.append(animal)
print(animal)







# --- Print results --- #
cage = "+===============+"
index = 0
print("ZOO MAP:")
print(cage)
while index < len(animals):
    row = "| " + animals[index]
    spaces = 14 - len(animals[index])
    while spaces > 0:
        row += " "
        spaces -= 1
    row += "|"
    print(row)
    print(cage)
    index += 1


# Turn in your Coding Exercise.
