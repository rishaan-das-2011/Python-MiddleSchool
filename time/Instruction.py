"""
LESSON: 3.6 - Time
INSTRUCTION 1
"""

# Libraries
import pygame
pygame.init()

# Variables
w = pygame.display.set_mode([200, 200])
c = pygame.time.Clock()
clicks = 0
frames = 0
timer = 0

# Main loop
while clicks < 10:
    frames += 1

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clicks = 100

        # Record clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
    c.tick(60)
    timer += c.get_time()

# Print final frames
print("You took " + str(frames) + " frames to click 10 times")
print("That's " + str(timer / 1000) + " seconds! ")
