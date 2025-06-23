"""
LESSON: 6.1 - Functions
WARMUP 6
"""

# Libraries
import random
import pygame
pygame.init()


#### ---------------------------------- ####
#### ---- DRAW ONE CIRCLE FUNCTION ---- ####
#### ---------------------------------- ####

def draw_one_circle(x, y):
    circle_x = x + (random.randint(-50, 50))
    circle_y = y + (random.randint(-50, 50))
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    pygame.draw.circle(w, (red, green, blue), (circle_x, circle_y), random.randint(10, 40))









#### ------------------------------- ####
#### ---- DRAW CIRCLES FUNCTION ---- ####
#### ------------------------------- ####

def draw_circles(x, y):
    for i in range(5):
        draw_one_circle(x, y)



#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

w = pygame.display.set_mode([1018, 573])
w.fill((255, 255, 255))

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Call function here

            draw_circles(x, y)

    # Finish
    pygame.display.flip()

