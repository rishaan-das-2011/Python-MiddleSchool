"""
LESSON: 6.2 - Return Values
EXERCISE: Lost in Translation
"""

#### ---------------------------- ####
#### ---- PIG LATIN FUNCTION ---- ####
#### ---------------------------- ####

# DEFINE the pig_latin function with PARAMETER base

def pig_latin(base):

    # Create a list of vowels: "a", "e", "i", "o", "u",
    # and "y"
    
    vowels = ["a", "e", "i", "o", "u", "y"]

    # Create variable at_vowel that starts as False
    
    at_vowel = False

    # Create variable word_start as an empty string
    
    word_start = ""

    # Create variable word_end as an empty string
    
    word_end = ""


    # --- Find the first vowel --- #

    # For each letter in base
    
    for letter in base:

        # If letter is in the vowels list
        
        if letter in vowels:
       
            # Set at_vowel to True
        
            at_vowel = True


        # --- Add current letter to word segment --- #

        # If not at_vowel
        
        if not at_vowel:

            # Increment word_end by letter
            
            word_end += letter

        # Else
        
        else:

            # Increment word_start by letter
            
            word_start += letter


    # --- Combine segments into final words --- #

    # Set the final_word to the word_start concatenated
    # to word_end concatenated to "ay"
    
    final_word = (str(word_start) + "ay")

    # RETURN final_word
    # ---> TEST AFTER THIS LINE <--- #
    
    return final_word


#### ----------------------------- ####
#### ---- UBBI DUBBI FUNCTION ---- ####
#### ----------------------------- ####

# DEFINE ubbi_dubbi function with PARAMETER base

def ubbi_dubbi(base):

    # Create a list of vowels: "a", "e", "i", "o", "u"
    # and "y"
    
    vowels = ["a", "e", "i", "o", "u", "y"]

    # Create variable final_word as an empty string
    
    final_word  = ""

    # Create variable this_letter_vowel that starts as
    # False
    
    this_letter_vowel = False

    # Create variable prev_letter_vowel that starts as
    # False
    
    prev_letter_vowel = False


    # --- Go through letters --- #

    # For letter in base
    
    for letter in base:

        # --- Check if last letter was a vowel --- #

        # Set prev_letter_vowel to this_letter_vowel
        
        prev_letter_vowel = this_letter_vowel


        # --- Check if this letter is a vowel --- #

        # If letter is in vowels
        
        if letter in vowels:


            # Set this_letter_vowel to True
            
            this_letter_vowel = True

        # Else
        
        
        else:

            # Set this_letter_vowel to False
            
            this_letter_vowel = False


        # --- Add "ubb" in front of vowel sets --- #

        # If not this_letter_vowel or prev_letter_vowel
        
        if not this_letter_vowel or not prev_letter_vowel:

            # Increment final_word by letter
            
            final_word += letter

        # Else
        
        else:

            # Increment final_word by "ubb" + letter
            
            final_word  += ("ubb" + letter)

    # RETURN final_word
    # ---> TEST AFTER THIS LINE <--- #
    
    return final_word


#### -------------------------- ####
#### ---- REVERSE FUNCTION ---- ####
#### -------------------------- ####

# DEFINE reverse function with PARAMETER base

def reverse(base):

    # Set final_word to an empty string
    
    final_word = ""


    # --- Go through string in reverse --- #

    # For i in range length of base -1, with limit -1
    # and increment -1
    
    for i in range(len(base) - 1, -1, -1):
       

        # Increment final_word by the item from base
        # at index i
        
        final_word += base[i]

    # RETURN final_word
    # ---> TEST AFTER THIS LINE <--- #
    
    return final_word


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Get input --- #

# Ask the user "Enter a word to translate: " and assign
# the result to word

word = input("Enter a word to translate: ")

# Print a blank line
# ---> TEST AFTER THIS LINE <--- #

print()


# --- Print translations --- #

# Print "PIG LATIN: " + the result of CALLing pig_latin
# with word

print("PIG LATIN: " + pig_latin(word))

# Print "UBBI DUBBI: " + the result of CALLing
# ubbi_dubbi with word

print("UBBI DUBBI: "+ ubbi_dubbi(word))

# Print "REVERSE: " + the result of CALLing reverse
# with word

print("Reverse: " + reverse(word))




# Turn in your Coding Exercise.
