"""
LESSON: 5.4 - Sprites in Lists
WARMUP 1
"""
import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
gem_names = ["RoundGemBlue.png", "RoundGemRed.png", "RoundGemBrown.png", "RoundGemPink.png"]

# Create a list of gems
gems = []

# Create 15 random gems at random locations

for i in range(15):
    g = tsk.Sprite(random.choice(gem_names), random.randint(0, 1018), random.randint(0, 573))
    gems.append(g)
    
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()

    # Draw all the gems
    for g in gems:
        g.draw()

    pygame.display.flip()

    c.tick(30)