"""
LESSON: 5.1 - Sprites
WARMUP 1
"""
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Draw colors and shapes here

    window.fill((0, 0, 0))
    r = pygame.Rect(0, 287, 1018, 287)
    pygame.draw.rect(window, (110, 70, 60), r)
    pygame.draw.circle(window, (255, 240, 150), (509, 287), 250)
    pygame.display.flip()
