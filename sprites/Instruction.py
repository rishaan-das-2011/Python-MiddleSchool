"""
LESSON: 5.1 - Sprites
INSTRUCTION 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
cat = tsk.Sprite("Cat.png", 400, 200)
cat.scale = 50
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Draw colors and shapes here
    window.fill((0, 0, 0))
    x, y = cat.center
    y += 1
    cat.center = (x, y)
    r = pygame.Rect(0, 300, 1018, 300)
    pygame.draw.rect(window, (110, 70, 60), r)
    pygame.draw.circle(window, (255, 240, 150), (509, 286), 250)
    cat.draw()
    pygame.display.flip()
    pygame.time.wait(50)