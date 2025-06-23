"""
LESSON: 4.1 - Lists
EXERCISE: Code Your Own
Among Us SpaceShip
"""


import random

players = []

name = ""


while name != "done":
    
    name = input("Enter a name (or 'done' to finish): ")

    if name == "done":

        break
    if name != "" and name not in players:
        players.append(name)


pick = random.randint(0, len(players) - 1)


impostor = players[pick]


while len(players) > 1:


    print("Players: " + str(players))


    attempt = input("Who do you think is the Impostor? ")


    if attempt == impostor:

        print("Congratulations! You have found the impostor. ")
        break


    elif attempt in players:

        print("Sorry, that is not the impostor. ")
        players.remove(attempt)


if len(players) == 1:


    print("Game over! You failed to find the Impostor. The Impostor was " + impostor + ".")


# Turn in your Coding Exercise.
