"""
LESSON: 4.2 - For Each
TECHNIQUE 2: Count Items
PRACTICE 2
"""

import pygame
import random
pygame.init()

# --- User input --- #
shapes = []
shape = ""
while shape.lower() != "done":
    shape = input("Enter a shape (done to stop): ")
    if shape.lower() != "done":
        shapes.append(shape)

# --- Count circles and squares --- #
circles = 0
squares = 0

# Loop through the list of shapes and count all the squares and circles
for i in shapes:
    if i == "circle":
        circles += 1
    elif i == "square":
        squares += 1

# --- Display results --- #
window = pygame.display.set_mode([500, 500])
window.fill((60, 60, 60))

while circles > 0:
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    r = random.randint(80, 255)
    g = random.randint(80, 255)
    b = random.randint(80, 255)
    pygame.draw.circle(window, (r, g, b), (x, y), 50)
    circles -= 1

while squares > 0:
    x = random.randint(-50, 450)
    y = random.randint(-50, 450)
    r = random.randint(80, 255)
    g = random.randint(80, 255)
    b = random.randint(80, 255)
    square = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(window, (r, g, b), square)
    squares -= 1

pygame.display.flip()
pygame.time.wait(4000)


# Turn in your Coding Exercise.
