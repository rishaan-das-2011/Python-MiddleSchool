"""
LESSON: 4.3 - For Range
TECHNIQUE 1: Generate a List
PRACTICE 1
"""

import random

# --- Get input and build list --- #

player_number = int(input("How many players are there? "))
players = []

# Make a loop that counts up to the player_number,
# adding a new string to the list of players for each
for i in range(player_number):
    
    players.append("Player: " + str(i))


# --- Print in random order --- #
print()
print("Here is your random order:")
while len(players) > 0:
    index = random.randint(0, len(players) - 1)
    print(players[index])
    players.remove(players[index])


# Turn in your Coding Exercise.
