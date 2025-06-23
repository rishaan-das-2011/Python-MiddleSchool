"""
LESSON: 4.3 - For Range
EXERCISE: Code Your Own

TITLE: Number Picking Game
DESCRIPTION: Prompt shows 10 random numbers between 1 and 100 for two players
to choose from. When it's the player's turn, the
number is blanked from the kernel, and who ever picks 
the higher number wins that round. Whoever wins 
the most rounds wins the game.
"""
import random

ListRandomNumber = []

print("Welcome to the number picking game! ")
NumberOfRound = int(input("Please enter number of rounds: "))

for number in range(NumberOfRound):
    NumberIn = random.randint(1, 100)
    if NumberIn in ListRandomNumber:
        ListRandomNumber.append(NumberIn + 1) # To avoid repitation of numbers
    else:
        ListRandomNumber.append(NumberIn)
        
    
player1_moves = list(ListRandomNumber)
player2_moves = list(ListRandomNumber)


wins1 = 0
wins2 = 0
ties = 0



for i in range(NumberOfRound):
    print("Avaiable move: " + str(player1_moves))
    player1 = int(input("Player 1, pick a number: "))
    
    
    while player1 not in player1_moves:
        player1 = int(input("Invalid move! Pick a number from the list "))

    player1_moves.remove(player1)
    print("\n" * 100)



    print("Available moves: " + str(player2_moves))
    player2 = int(input("Player 2, pick a number: "))


    while player2 not in player2_moves:
        player2 = int(input("Invalid move! Pick a number from the list!"))


    player2_moves.remove(player2)


    print()

    print("Player 1 chose " + str(player1) + " and Player 2 chose " + str(player2))

    if player1 == player2:
        ties += 1
        print("No one wins this round! ")
        
    elif player1 > player2:
        wins1 += 1
        print("Player 1 wins this round! ")


    else:
        wins2 += 1
        print("Player 2 wins this round! ")


    print()



if wins1 > wins2:
    print("Player 1 wins the game! ")


elif wins2 > wins1:
    print("Player 2 wins the game! ")


else:
    print("The game is a tie!" )


# Turn in your Coding Exercise.