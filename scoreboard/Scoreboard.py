"""
LESSON: 6.1 - Functions
EXERCISE: Scoreboard
"""

#### -------------------------------- ####
#### ---- PRINT MIN/MAX FUNCTION ---- ####
#### -------------------------------- ####

# DEFINE the print_min_max function with PARAMETERS
# all_scores, all_players, and which_score

def print_min_max(all_scores, all_players, which_score):

    # — Validate arguments — #
    # If the length of all_scores is 0
    
    if len(all_scores) == 0:
        
        # Print "No scores yet entered"
        
        print("No scores yet entered. ")
        
        # Return
        
        return

    # — Starting defaults — #
    # Set min to the first entry in all_scores
    
    mini = all_scores[0]
    
    # Set max the first entry in all_scores
    
    maxi = all_scores[0]
    
    # Set min_person to the first entry in all_players
    
    min_person = all_players[0]
    
    # Set max_person to the first entry in all_players
    
    max_person = all_players[0]

    # — Find min and max — #
    # For i in range length of all_scores
    
    for i in range(len(all_scores)):
        
        # Set score to the item from all_scores at index position i
        
        score = all_scores[i]

        # If score is less than min
        
        if score < mini:
            
            # Set min to score
            
            mini = score
            
            # Set min_person to the item from all_players at index position i
            
            min_person = all_players[i]
    
        # If score is greater than max
        
        if score > maxi:
            
            # Set max to score
            
            maxi = score
            
            # Set max_person to the item from all_players at index position i
            max_person = all_players[i]

    # — Print relevant score(s) — #
    # If which_score is "min" or "both"
    
    if which_score == "min" or which_score == "both":
        
        # Print "LOWEST SCORE: " + min_person + ", with " + min converted to a string
        
        print("LOWEST SCORE: " + min_person + ", with " + str(mini))

    # If which_score is "max" or "both"
    
    if which_score == "max" or which_score == "both":
        
        # Print "HIGHEST SCORE: " + max_person + ", with " + max converted to a string
        
        print("HIGHEST SCORE: " + max_person + ", with " + str(maxi))

#### ------------------------------- ####
#### ---- PRINT SCORES FUNCTION ---- ####
#### ------------------------------- ####

# DEFINE print_scores function with PARAMETERS
# all_scores and all_players

def print_scores(all_scores, all_players):

    # — Validate arguments — #
    # If the length of all_scores is 0
    
    if len(all_scores) == 0:
        
        # Print "No scores yet entered"
        
        print("No scores yet entered. ")
        
        # Return
        
        return

    # — Print all scores — #
    # Print "ALL SCORES"
    
    print("ALL SCORES")
    
    # Print a line of dashes "--------------------------"
    
    print("--------------------------")
    
    # For i in range length of all_scores
    
    for i in range(len(all_scores)):
        
        # Print the item from all_players at index i + ": " + the item from all_scores at index i converted to a string
        
        print(all_players[i] + ": " + str(all_scores[i]))

#### -------------------------------- ####
#### ---- PRINT SUMMARY FUNCTION ---- ####
#### -------------------------------- ####

# DEFINE the print_summary function with PARAMETERS
# all_scores and all_players

def print_summary(all_scores, all_players):
    
    # Print "SCORE SUMMARY"
    
    print("SCORE SUMMARY")
    
    # Print a line of dashes "--------------------------"
    
    print("--------------------------")
    
    # Print "TOTAL NUMBER OF SCORES: " + the length of all_scores converted to a string
    
    print("TOTAL NUMBER OF SCORES: " + str(len(all_scores)))
    
    # CALL print_min_max with all_scores, all_players, and "both"
    
    print_min_max(all_scores, all_players, "both")

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####

# Create an empty list called names

names = []

# Create an empty list called scores

scores = []


#### ---- MAIN LOOP ---- ####

done = False
while not done:

    #### ---- MENU ---- ####
    print()
    print("---- MENU ----")
    print("What would you like to do?")
    print("   1: Enter a new player & score")
    print("   2: Get the current highest score")
    print("   3: Get the current lowest score")
    print("   4: Print all scores")
    print("   5: Print a full summary")
    print("   0: Quit")
    user_choice = input()
    print()

    if user_choice == "0":
        done = True

    #### ---- INPUT SCORES ---- ####
    
    elif user_choice == "1":
        
        # Set variable name to the result of input with prompt "Enter a player name: "
        
        name = input("Enter a player name: ")
        
        # Set variable score to the result of input typecast to an int with prompt "Enter a player score: "
        
        score = int(input("Enter a player score: "))
        
        # Append name to the names list
        
        names.append(name)
        
        # Append score to the scores list
        
        scores.append(score)

    #### ---- GET STATS ---- ####
    
    elif user_choice == "2":
        
        # CALL print_min_max with scores, names, and "max" as arguments
        
        print_min_max(scores, names, "max")
        
    elif user_choice == "3":
        
        # CALL print_min_max with scores, names, and "min" as arguments
        
        print_min_max(scores, names, "min")
        
    elif user_choice == "4":
        
        # CALL print_scores with scores and names
        print_scores(scores, names)
        
    elif user_choice == "5":
        
        # CALL print_summary with scores and names
        print_summary(scores, names)
        
    else:
        print("I'm sorry, that was not a valid choice")


# Turn in your Coding Exercise.



