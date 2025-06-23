"""
LESSON: 4.2 - For Each
TECHNIQUE 2: Count Items
PRACTICE 1
"""

# --- User input --- #
numbers = []
number = 0
while True:
    number = input("Enter numbers (done to stop): ")
    if number == "done":
        break
    else:
        numbers.append(int(number))

# --- Count odd numbers --- #
# Loop through the list of numbers and count all the ones that are odd
odd_count = 0
for num in numbers:
    if num % 2 != 0:
        odd_count += 1
        
        

# --- Print results --- #
print("Out of " + str(len(numbers)) + " numbers,")

# Print how many numbers are odd
print("The number of odd numbers is: " + str(odd_count) + ".")


# Turn in your Coding Exercise.
