"""
LESSON: 6.1 - Functions
EXERCISE: Code Your Own

TITLE: The Great Mingler
DESCRIPTION: This is a relatively simple code, which
takes a user-input name, shuffles letters, and displays both the original 
and shuffled versions.
"""

import random

### Shuffles the characters in a string and returns the result. ###
def shuffle_letters(input_string):  

    
    
    char_list = list(input_string)
    random.shuffle(char_list)
    
    # Unites the words and seperates them
    return ''.join(char_list) 

### Main program that handles user input and displays shuffled name ###

def main():
    
    
    
    # Validation loop
    
    while True:
        user_name = input("Enter a name to shuffle: ")
        
        # Checks whether the user is entering a valid string
        if not user_name:  
            print("Please enter a name.")
        
        else:
            # Calling the function [with a parameter] to return the shuffled string
            mixed = shuffle_letters(user_name) 
            # The '\n' adds a new line when run
            print("\nOriginal: " + user_name) 
            print("Shuffled: " + mixed)
            break

if __name__ == "__main__":
    main()