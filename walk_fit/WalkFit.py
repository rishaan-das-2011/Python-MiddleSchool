"""
LESSON: 4.2 - For Each
EXERCISE: Walk Fit
"""

#### ---- SETUP ---- ####

# Create a list containing the days of the week and
# assign to the variable week

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create an empty list and assign to miles_per_day
# ---> TEST AFTER THIS LINE <--- #
miles_per_day = []


#### ---- USER INPUT ---- ####

# FOR EACH variable day in the list week
for day in week:

    # Create variable miles and assign it input asking
    # how many miles the user walked on variable day
    miles = input("How many miles did you walk " + day + "?")

    # Append miles typecasted to a float to the list
    # miles_per_day
    # ---> TEST AFTER THIS LINE <--- #
    miles_per_day.append(float(miles))


#### ---- CALCULATE FITNESS ---- ####

# --- Variables --- #

# Create variable total_miles and assign value 0
total_miles = 0

# Create variable total_calories and assign value 0
total_calories = 0


# --- Calculate sums --- #

# FOR EACH variable miles in list miles_per_day
for miles in miles_per_day:

    # Increment total_miles by miles
    total_miles += miles
    # Increment total_calories by miles * 70
    # ---> TEST AFTER THIS LINE <--- #
    total_calories += miles * 70


# --- Calculate averages --- #

# Assign variable avg_miles the value total_miles / the
# length of week

avg_miles = total_miles/len(week)

# Assign variable avg_cal the value total_calories /
# the length of week

avg_cal = total_calories / len(week)

#### ---- OUTPUT ---- ####

# --- Intro --- #

# Print a blank line

print()

# Print a title for the fitness stats

print("Fitness Stats: ")

# Print a line of dashes

print("-----------")

# --- Stats --- #

# Print message with total_miles converted to a string

print("Total miles walked: " + str(total_miles))

# Print message with total_calories converted to a
# string

print("Total calories burned: " + str(total_calories))

# Print message with avg_miles converted to a string

print("Average miles walked per day: " + str(avg_miles))

# Print message with avg_cal converted to a string
# ---> TEST AFTER THIS LINE <--- #


print("Average calories burned per day: " + str(avg_cal))


# Turn in your Coding Exercise.
