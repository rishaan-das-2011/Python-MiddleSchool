"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Code Your Own

TITLE: A Bird's Nest
DESCRIPTION: Once ran, a nest and a bush appears in a meadow. 
A bird spawns every second. 
The bees fly to the bush and back until it dissapears.
"""

import tsk
import random
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
background = tsk.Sprite("FlowerMeadow.jpg", 0, 0)
bird_nest = tsk.Sprite("BirdNest.png", -80, 250)
flowerbush = tsk.Sprite("Bush.png", 620, 250)
birds_leaving = []
birds_returning = []
bird_spawn_time = 1000
timer = 0
bird_speed = 0.2
maximum_birds = 10

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            drawing = False

    timer += c.get_time()
    if timer > bird_spawn_time:
        timer = 0
        if len(birds_leaving) + len(birds_returning) < maximum_birds:
            bird = tsk.Sprite("Hummingbird.png", bird_nest.center_x, random.randint(200, 350))
            birds_leaving.append(bird)

    for bird in birds_leaving:
        bird.center_x += bird_speed * c.get_time()
        if bird.center_x > flowerbush.center_x:
            bird.flip_x = True
            birds_leaving.remove(bird)
            birds_returning.append(bird)

    done_birds = []
    for bird in birds_returning:
        bird.center_x -= bird_speed * c.get_time()
        if bird.center_x < bird_nest.center_x:
            done_birds.append(bird)

    for bird in done_birds:
        birds_returning.remove(bird)

    background.draw()
    bird_nest.draw()
    flowerbush.draw()
    for bird in birds_leaving:
        bird.draw()
    for bird in birds_returning:
        bird.draw()
    pygame.display.flip()
    c.tick(30)

# Turn in your Coding Exercise.

