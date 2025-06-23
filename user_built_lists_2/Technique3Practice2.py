"""
LESSON: 4.1 - Lists
TECHNIQUE 3: User-Built Lists
PRACTICE 2
"""


# --- Setup --- #
import pygame
pygame.init()

x_positions = []
y_positions = []

# --- Enter points --- #

# Until the user enters "done", get two numbers as
# input, storing each to x_positions and y_positions

while True:
    user_input_x = input("Enter x coordinates. (type done to exit)")
    user_input_y = input("Enter y coordinates.")
    if user_input_x.lower() == 'done':
        break
    x_positions.append(user_input_x)
    y_positions.append(user_input_y)








# --- Main loop --- #
window = pygame.display.set_mode([500, 500])
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Draw --- #
    index = 1
    while index < len(x_positions):
        p1 = (int(x_positions[index]), int(y_positions[index]))
        p2 = (int(x_positions[index - 1]), int(y_positions[index - 1]))
        pygame.draw.line(window, (0, 0, 0), p1, p2, 5)
        index += 1

    pygame.display.flip()