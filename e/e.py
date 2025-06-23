"""
LESSON: TechSmart Studio Project
"""

#### ---- SETUP ---- ####

# --- Libraries --- #

# A1: Import and initialize pygame

import pygame
pygame.init()

# --- General variables --- #
# A2: Create variables width and height each with value
# 600

width = 600
height = 600


# C1: Create variable drawing with value True

drawing = True

# D1: In C1, start drawing as False

drawing = False

# --- Color variables --- #

# B1: Create a LIST containing the following color
# tuples and assign it to variable colors:
# (0, 0, 0), (255, 255, 255), (255, 0, 0),
# (255, 130, 0), (255, 255, 0), (0, 255, 0),
# (0, 255, 255), (0, 0, 255), (150, 50, 255),
# (255, 0, 255), (255, 150, 200), (150, 75, 0)

colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 130, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (150, 50, 255), (255, 0, 255), (255, 150, 200), (150, 75, 0)]


# C2: Create variable draw_color and assign it INDEX 0
# of the colors list, and variable draw_size with
# value 10

draw_color = colors[0]
draw_size = 10

# --- Color positions ---- #
# B2: Create variable color_width and assign it value
# width / LEN of colors typecast to an int


color_width = int(width / len(colors))

# B3: Create an empty LIST called color_positions. Then,
# FOR i in RANGE LEN of colors, APPEND i * color_width
# to color_positions.


color_positions = []
for i in range(len(colors)):
    color_positions.append(i * color_width)
    
# --- Window --- #
# A3: Open a window of size [width, height] and fill it
# with white

window = pygame.display.set_mode([width, height])
window.fill((255, 255, 255))


#### ---- MAIN LOOP ---- ####
# A4: Assign variable done the value False and loop
# while not done

done = False
while not done:

    # --- Mouse Position --- #    
    
    # C3: Assign x, y the mouse position
    x, y = pygame.mouse.get_pos()   
    
    
    # --- Event Loop --- #
    
    # A5: Create an event loop that sets done to True
    # when the QUIT event type occurs
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Fixed from False to True
        #### ---- MOUSE EVENTS ---- ####
        # --- Mouse down --- #
        # D2: Elif the event type is MOUSEBUTTONDOWN
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # --- Clicked in circle --- #
            
            # D3: If y is greater than 30, set drawing
            # to True
            
            if y > 30:
                drawing = True
            # --- Clicked in palette --- #
            # E1: Else
            else:
                
                # E2: FOR i in RANGE LEN of
                # color_positions
                
                for i in range(len(color_positions)):
                    # E3: Assign edge the value at
                    # INDEX i of color_positions
                    edge = color_positions[i]
                    # E4: If edge is less than x and x
                    # is less than edge + color_width
                    
                    if edge < x and x < edge + color_width:  # Fixed comparison operators
                        # E5: Assign draw_color the
                        # value at INDEX i of colors,
                        # and break out of the loop
                        # ---> TEST AFTER THESE LINES <--- #
                        draw_color = colors[i]
                        
                        break
        # --- Mouse up --- #
        # D4: Elif the event type is MOUSEBUTTONUP,
        # set drawing to False
        # ---> TEST AFTER THESE LINES <--- #
        
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            
        #### ---- KEYBOARD EVENTS ---- ####
        # F1: Elif the event type is KEYDOWN
        
        elif event.type == pygame.KEYDOWN:
            
            # --- Change size --- #
            # F2: If the event key is UP, increment
            # draw_size by 2
            
            if event.key == pygame.K_UP:  # Fixed to check event.key, not event.type
                draw_size += 2
                
            # F3: Elif the event key is DOWN, decrement
            # draw_size by 2
            
            elif event.key == pygame.K_DOWN:  # Fixed to check for K_DOWN
                draw_size -= 2
        
            # --- Limit min and max size --- #
            # F4: If draw_size is less than 2, set it
            # to 2
            
            if draw_size < 2:
                draw_size = 2
            # F5: If draw_size is greater than 100, set
            # it to 100
            # ---> TEST AFTER THESE LINES <--- #
            
            if draw_size > 100:
                draw_size = 100
    #### ---- DRAW ---- ####
    
    # --- Draw circle --- #
    # C4: If drawing, draw a circle with draw_color
    # at position (x, y) with radius draw_size
    # ---> TEST AFTER THESE LINES <--- #
    
    if drawing:
        pygame.draw.circle(window, draw_color, (x, y), draw_size) 
    # --- Draw color palette --- #
    # B4: FOR i in RANGE LEN of colors
    
    for i in range(len(colors)):
        
        # B5: Assign variable position the value at
        # INDEX i of color_positions
        
        
        position = color_positions[i]
        # B6: Create and draw a rectangle at position,
        # 0, with width color_width and height 30,
        # using color from colors list at INDEX i
        # ---> TEST AFTER THESE LINES <--- #
        
        r = pygame.Rect(position, 0, color_width, 30)
        pygame.draw.rect(window, colors[i], r)
        
    # --- Finish drawing --- #
    
    
    # A6: Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    
    pygame.display.flip()
    
    
# Turn in your Coding Project.
