"""
LESSON: 6.1 - Functions
WARMUP 4
"""

import random

#### ------------------------------- ####
#### ---- PRINT ANIMAL FUNCTION ---- ####
#### ------------------------------- ####
def animal_name():
    animals = ["frog", "dog", "horse", "chicken"]
    print(random.choice(animals))





#### ------------------------------ ####
#### ---- PRINT NOISE FUNCTION ---- ####
#### ------------------------------ ####

def animal_sound():
    sounds = ["Moo", "Ruff", "Meow", "Quack", "Oof"]
    print(random.choice(sounds))




#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

q = ""

# Main loop
while q != "quit":

    print("The most popular animal on our farm is our: ")

    # Call the print animal function here

    animal_name()

    print()

    print("People come from everywhere to hear it say: ")

    # Call the print noise function here

    animal_sound()

    print()
    q = input("(Enter or type quit) ")
    print()