"""
LESSON: 6.1 - Functions
TECHNIQUE 3: Draw at Offset
PRACTICE 1
"""

import random
import pygame
import math

pygame.init()

#### ------------------------------- ####
#### ---- DRAW DIAMOND FUNCTION ---- ####
#### ------------------------------- ####

def draw_diamond(window, center_x, center_y):
    shift_x = center_x + 75
    shift_y = center_y + 0
    pt1 = (-100 + shift_x, 0 + shift_y)
    pt2 = (-75 + shift_x, 30 + shift_y)
    pt3 = (-50 + shift_x, 0 + shift_y)
    pt4 = (-75 + shift_x, -30 + shift_y)
    pygame.draw.polygon(window, (255, 0, 0), [pt1, pt2, pt3, pt4])

#### ----------------------------- ####
#### ---- DRAW HEART FUNCTION ---- ####
#### ----------------------------- ####

def draw_heart(window, center_x, center_y):
    shift_x = center_x - 75
    shift_y = center_y + 5
    pt1 = (100 + shift_x, 0 + shift_y)
    pt2 = (50 + shift_x, 0 + shift_y)
    pt3 = (75 + shift_x, 30 + shift_y)
    circle_left = (62 + shift_x, -5 + shift_y)
    circle_right = (88 + shift_x, -5 + shift_y)
    pygame.draw.polygon(window, (255, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (255, 0, 0), circle_left, 14)
    pygame.draw.circle(window, (255, 0, 0), circle_right, 14)

#### ---------------------------- ####
#### ---- DRAW CLUB FUNCTION ---- ####
#### ---------------------------- ####

def draw_club(window, center_x, center_y):
    shift_x = center_x
    shift_y = center_y - 70
    pt1 = (-21 + shift_x, 97 + shift_y)
    pt2 = (21 + shift_x, 97 + shift_y)
    pt3 = (0 + shift_x, 77 + shift_y)
    circle_left = (-14 + shift_x, 70 + shift_y)
    circle_right = (14 + shift_x, 70 + shift_y)
    circle_top = (0 + shift_x, 50 + shift_y)
    pygame.draw.polygon(window, (0, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (0, 0, 0), circle_left, 16)
    pygame.draw.circle(window, (0, 0, 0), circle_right, 16)
    pygame.draw.circle(window, (0, 0, 0), circle_top, 16)

#### ----------------------------- ####
#### ---- DRAW SPADE FUNCTION ---- ####
#### ----------------------------- ####

def draw_spade(window, center_x, center_y):
    shift_x = center_x
    shift_y = center_y + 70
    pt1 = (-21 + shift_x, -45 + shift_y)
    pt2 = (21 + shift_x, -45 + shift_y)
    pt3 = (0 + shift_x, -65 + shift_y)
    pt4 = (-29 + shift_x, -75 + shift_y)
    pt5 = (29 + shift_x, -75 + shift_y)
    pt6 = (0 + shift_x, -110 + shift_y)
    circle_left = (-14 + shift_x, -70 + shift_y)
    circle_right = (14 + shift_x, -70 + shift_y)
    pygame.draw.polygon(window, (0, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (0, 0, 0), circle_left, 16)
    pygame.draw.circle(window, (0, 0, 0), circle_right, 16)
    pygame.draw.polygon(window, (0, 0, 0), [pt4, pt5, pt6])

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
timer = 2000
x = 500
y = 250
radius = 100  

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Update location every 2 seconds
    if timer <= 0:
        timer = 2000
        x = random.randint(100, 900)
        y = random.randint(100, 450)

    # Clear the screen
    w.fill((255, 255, 255))

    # Calculate positions for each shape around the central point (x, y)
    diamond_pos = (x + radius, y)       # To move right
    heart_pos = (x, y - radius)         # Top move up
    club_pos = (x - radius, y)          # To move left
    spade_pos = (x, y + radius)         # To move down

    # Draw each suit at their respective positions
    draw_diamond(w, * diamond_pos)
    draw_heart(w, * heart_pos)
    draw_club(w, * club_pos)
    draw_spade(w, * spade_pos)

    # Update timer and display
    timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)

#### ------------------------------- ####
#### ---- DRAW DIAMOND FUNCTION ---- ####
#### ------------------------------- ####
def draw_diamond(window):
    pt1 = (-100, 0)
    pt2 = (-75, 30)
    pt3 = (-50, 0)
    pt4 = (-75, -30)
    pygame.draw.polygon(window, (255, 0, 0), [pt1, pt2, pt3, pt4])


#### ----------------------------- ####
#### ---- DRAW HEART FUNCTION ---- ####
#### ----------------------------- ####
def draw_heart(window):
    pt1 = (100, 0)
    pt2 = (50, 0)
    pt3 = (75, 30)
    circle_left = (62, -5)
    circle_right = (88, -5)
    pygame.draw.polygon(window, (255, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (255, 0, 0), (circle_left), 14)
    pygame.draw.circle(window, (255, 0, 0), (circle_right), 14)


#### ---------------------------- ####
#### ---- DRAW CLUB FUNCTION ---- ####
#### ---------------------------- ####
def draw_club(window):
    pt1 = (-21, 97)
    pt2 = (21, 97)
    pt3 = (0, 77)
    circle_left = (-14, 70)
    circle_right = (14, 70)
    circle_top = (0, 50)
    pygame.draw.polygon(window, (0, 0, 0), [pt1, pt2, pt3])
    pygame.draw.circle(window, (0, 0, 0), (circle_left), 16)
    pygame.draw.circle(window, (0, 0, 0), (circle_right), 16)
    pygame.draw.circle(window, (0, 0, 0), (circle_top), 16)


#### ----------------------------- ####
#### ---- DRAW SPADE FUNCTION ---- ####
#### ----------------------------- ####
# Turn in your Coding Exercise.
