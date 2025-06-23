"""
LESSON: 4.3 - For Range
TECHNIQUE 2: Counting Down
PRACTICE 1
"""
import pygame
pygame.init()

# Print a countdown until the New Year

for seconds in range (10, 0, -1):
    print(str(seconds) + " seconds are left...")
    pygame.time.wait(1000)



# Happy New Year!
print("\o/ Happy New Year! \o/")


# Turn in your Coding Exercise.
