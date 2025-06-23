"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 3: Sprite Walls
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
ship_sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
ship = tsk.Sprite(ship_sheet, 100, 300)
barrier = tsk.Sprite("ForceBarrier.png", 600, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if tsk.is_key_down(pygame.K_LEFT):
        ship.center_x -= 0.2 * c.get_time()

        if ship.rect.left < 0:
            ship.center_x = ship.rect.width / 2


    if tsk.is_key_down(pygame.K_RIGHT):
        ship.center_x += 0.2 * c.get_time()

        if ship.rect.right > barrier.rect.left:
            ship.center_x = barrier.rect.left - (ship.rect.width / 2)


    background.draw()
    barrier.draw()
    ship.draw()
    ship.update(c.get_time())

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
