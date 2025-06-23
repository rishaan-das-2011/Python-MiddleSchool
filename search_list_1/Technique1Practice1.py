"""
LESSON: 4.2 - For Each
TECHNIQUE 1: Search List
PRACTICE 1
"""

# --- User input --- #
pets = []
pet = ""
while pet != "done":
    pet = input("Enter the pets you have (done to finish): ")
    if pet != "done":
        pets.append(pet)

# --- Find a pet --- #

# Search pets for the word "dog"
dog_found = False
for pet in pets:
    if pet == "dog":
        dog_found = True
        break
    


# --- Print results --- #
print("Here are your pets:")
print(pets)

# Print message if dog was found
if dog_found:   
    print("You have a dog!")
else:
    print("You don't have a dog.")

# Turn in your Coding Exercise.
