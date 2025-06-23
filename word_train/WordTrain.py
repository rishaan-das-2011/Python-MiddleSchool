"""
LESSON: 4.2 - For Each
EXERCISE: Word Train
"""

#### ---- SETUP ---- ####

# --- Variables --- #

# Create a variable used_letters and assign it an
# empty LIST

used_letters = []

# Create variable last_used and assign it the string "s"

last_used = "s"

# --- Print rules --- #

# Print a welcome message that explains the rules
# (listed in the assignment panel)
# ---> TEST AFTER THESE LINES <--- #

print("1) Players take turns entering words")
print("2) The first letter of each player's word must be the same as the last letter of the previous word")
print("3) If you repeat an ending letter that's already been used, you lose!")
print("Used letters: s,")
print("Please enter a word that begins with the letter s: ")





#### ---- GAME LOOP ---- ####

# while last_used is not IN list used_letters

while last_used not in used_letters:

    #### ---- PRINT USED LETTERS ---- ####

    # APPEND last_used to the list used_letters

    used_letters.append(last_used)

    # --- Assemble string of letters --- #

    # Assign string "Used letters: " to variable used

    used = "Used letters: "

    # FOR EACH letter in the list used_letters
    
    for letter in used_letters:

        # Increment used by letter + ", "

        used += letter + ", "

    # --- Print string --- #

    # Print a blank line

    print()

    # Print used

    print(used)


    #### ---- USER INPUT ---- ####

    # --- Get new word --- #

    # Ask the user to input a word beginning with the
    # letter last_used, and assign the result to word

    word = input("Enter a word that begins with " + last_used)

    # --- Get new last letter --- #

    # Assign last_used the letter from word at INDEX
    # LEN of word - 1
    # ---> TEST AFTER THIS LINE <--- #

    last_used = word[len(word) - 1]


#### ---- FINAL OUTPUT ---- ####

# Print a blank line

print()

# Print that the letter has already been used

print("The letter " + last_used + " has already been used!")

# Print "You got " + the LEN of used_letters TYPECAST
# to a STRing + " words!"
# ---> TEST AFTER THIS LINE <--- #

print("You got " + str(len(used_letters)) + " words!")



# Turn in your Coding Exercise.
