"""
LESSON: 6.3 - Complex Parameters
WARMUP 5
"""

#### --------------------------- ####
#### ---- GREETING FUNCTION ---- ####
#### --------------------------- ####

# Write a function that greets the user

def get_greeting(name = "pal"):
    print("Hello, " + name + "! ")


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
answer = input("Do you wish to enter a name? y/n ")

if answer == "y":
    user_name = input("Enter your name: ")

    # Call the function with the user's name

    get_greeting(user_name)

# Otherwise, call the function and let it use its
# default value

else: 
    get_greeting()
