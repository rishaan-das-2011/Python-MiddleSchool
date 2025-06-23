"""
LESSON: 6.3 - Complex Parameters
WARMUP 6
"""

#### ---------------------------------- ####
#### ---- ADD NOT ALLOWED FUNCTION ---- ####
#### ---------------------------------- ####

# Write a function that checks if a letter is already
# in a list and, if not, adds it to that list







#### ------------------------------ ####
#### ---- USED LETTER FUNCTION ---- ####
#### ------------------------------ ####
def used_letter(check_word, letter_list):
    for letter in check_word:
        if letter in letter_list:
            return True
    return False


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
forbidden_letters = []
lost = False

while not lost:
    letter = input("Enter a forbidden letter: ")

    # Call the add letter function with letter and
    # forbidden_letters


    print()
    word = input("Enter a word that doesn't use these letters: " + str(forbidden_letters) + " ")
    lost = used_letter(word, forbidden_letters)
    print()

print("Too bad! That contained a forbidden letter!")