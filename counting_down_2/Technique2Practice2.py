"""
LESSON: 4.3 - For Range
TECHNIQUE 2: Counting Down
PRACTICE 2
"""

# --- Setup window --- #
import pygame
pygame.init()
window = pygame.display.set_mode([500, 100])

background_color = (0, 0, 0)
bar_color = (255, 230, 200)

# --- Bar countdown --- #

# Count down from 10, drawing the bar
# 50 * i pixels wide each time
for i in range(10, 0, -1):
    window.fill(background_color)               
    bar_width = 50 * i                          
    bar_rect = pygame.Rect(0, 0, bar_width, 100)  
    pygame.draw.rect(window, bar_color, bar_rect)
    pygame.display.flip()                       
    pygame.time.wait(500)                      

# Turn in your Coding Exercise.
