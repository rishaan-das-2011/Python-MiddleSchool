"""
LESSON: 4.3 - For Range
TECHNIQUE 2: Counting Down
DEMO
"""

# --- Setup pygame --- #

import pygame
pygame.init()

# --- Prepare user for turn --- #
for i in range(5, 0, -1):
    distance = 100 * i
    print("In " + str(distance) + " feet, take a left.")
    pygame.time.wait(1000)



# --- Turn --- #
print("Turn left now. ")