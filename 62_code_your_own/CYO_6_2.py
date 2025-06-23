"""
LESSON: 6.2 - Return Values
EXERCISE: Code Your Own

TITLE: The Great Mingler
DESCRIPTION: This is a relatively simple code, which
takes user-input name(s), shuffles them, and displays both the original 
and shuffled versions.
"""

import random

### Shuffles the characters in a string and returns the result. ###

def shuffle_letters(input_string):



    char_list = list(input_string)
    random.shuffle(char_list)

    # Unites the words and seperates them
    return ''.join(char_list)

### Main program that handles user input and displays shuffled names ###

def main():



    # Validation loop

    #Ask user to enter number of name he wants to shuffle
    
    num = int(input("Enter how many names you want to shuffle: "))
    
    # Get all the names from user and enter into a list
    
    list_of_names = []

    for i in range (num):
        name = input("Enter a name to shuffle: ")
        list_of_names.append(name)

    # Call shuffle_letters function to suffle all the names using a map function
    # Calling as function expression
    print("\nThe shuffled name(s) are: " +  ', '.join(list(map(shuffle_letters, list_of_names))))

if __name__ == "__main__":
    main()
    
# Turn in your Coding Exercise.
