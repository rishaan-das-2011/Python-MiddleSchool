"""
LESSON: 4.2 - For Each
TECHNIQUE 3: Print List
DEMO
"""

elements = ["fire", "earth", "air", "water", "magnesium", "carbon"]

# --- Setup --- #
output = ""
count = 0

# --- Loop --- #
for elem in elements:
    output += str(elem)
    if count < len(elements)-1:
        output += ", "
    count += 1




# --- Print --- #
print(output)
