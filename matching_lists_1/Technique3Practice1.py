"""
LESSON: 4.3 - For Range
TECHNIQUE 3: Matching Lists
PRACTICE 1
"""

# --- Declare Lists --- #
items = []
prices = []

# --- User input --- #
print("Welcome to Menu Builder!")
item = ""
while item != "done":
    item = input("Enter an item (or done to end): ")
    if item == "done":
        break
    price = int(input("What is the item's price? "))
    items.append(item)
    prices.append(price)

# --- Print menu --- #
print()
print("MENU:")

# Loop through the lists of items and prices,
# and print each item with its price.

for i in range(len(items)): 
    print(str(items[i]) + ": $" + str(prices[i]))

# Turn in your Coding Exercise.
