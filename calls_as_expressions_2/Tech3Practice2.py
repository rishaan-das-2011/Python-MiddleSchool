"""
LESSON: 6.2 - Return Values
TECHNIQUE 3: Function Calls as Expressions
PRACTICE 2
"""
#### -------------------------- ####
#### ---- GET AGE FUNCTION ---- ####
#### -------------------------- ####
def get_age(birth_year, current_year):
    return current_year - birth_year
#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

total_age = 0
current_year = int(input("What is the current year? "))

# --- Get total ages of siblings --- #
siblings = int(input("How many siblings do you have? "))
for i in range(siblings):
    date = int(input("Enter a birth year sibling " + str(i + 1) + ": "))
    total_age += get_age(date, current_year)

# Write these lines as one line of code
date = int(input("What year were you born? "))
total_age += get_age(date, current_year)

# --- Calculate average --- #
avg_age = total_age / (siblings + 1)
print("The average age of you and your siblings is: " + str(avg_age))


# Turn in your Coding Exercise.
