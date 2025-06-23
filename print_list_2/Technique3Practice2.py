"""
LESSON: 4.2 - For Each
TECHNIQUE 3: Print List
PRACTICE 2
"""

gifts = ["four calling birds", "three french hens", "two turtle doves", "a partridge in a pear tree"]

# Loop through gifts, building a string with all its
# items.

gifts_str = ""

for i in range(len(gifts)):
    if i == len(gifts) -1:
        gifts_str += "and " + gifts[i]
    else:
        gifts_str += gifts[i] + ", "




# Print the string you built
print(gifts_str)

# Turn in your Coding Exercise.
