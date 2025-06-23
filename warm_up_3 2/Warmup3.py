"""
LESSON: 6.2 - Return Values
WARMUP 3
"""

import random

#### ------------------------------- ####
#### ---- GET GREETING FUNCTION ---- ####
#### ------------------------------- ####
def random_num(num):
    if num == 1:
        return "Hey, how are you?!"
    elif num == 2:
        return "Yo, wass good??"
    else:
        return "Hi."








#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
number = random.randint(1, 3)
print(random_num(number))