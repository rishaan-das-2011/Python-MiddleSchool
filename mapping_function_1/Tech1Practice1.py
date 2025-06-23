"""
LESSON: 6.2 - Return Values
TECHNIQUE 1: Mapping Function
PRACTICE 1
"""

#### ---- LIBRARIES ---- ####
import random


#### ------------------------------- ####
#### ---- GET GREETING FUNCTION ---- ####
#### ------------------------------- ####

def get_greeting(choice, name):
    if choice == 1:
        return "Hello, " + name + "." + " Have a wonderful day! "
    elif choice == 2:
        return "Good day, " + name + "." + " How may I assist you? "
    elif choice == 3:
        return "Yo, " + name + "! " + "What's new?"
    elif choice == 4:
        return "You were not supposed to choose this number. " 
    else:
        return "Please choose 1-4. "

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
name = input("What is your name? ")

while True:

    # Get input from the user
    greeting_choice = input("Type a number 1 - 4 or done: ")
    if greeting_choice == "done":
        break

    # Get a greeting based on the user's entered value
    try:
        choice_num = int(greeting_choice)
        greeting = get_greeting(choice_num, name)
        print(greeting)
        print()
    except ValueError:
        print("Please enter a valid number or 'done'")
        print()


# Turn in your Coding Exercise.
