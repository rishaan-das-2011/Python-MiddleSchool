"""
LESSON: 5.4 - Sprites in Lists
INSTRUCTION 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
puffin_sheet = tsk.ImageSheet("Puffin_Fly.png", 5, 6)
puffin = tsk.Sprite(puffin_sheet, 0, 200)
sprite_list = [puffin]



drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Check for mouse down and reset puffin here
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for sprite in sprite_list:
                if sprite.rect.collidepoint(mouse_x, mouse_y):
                    new_puffin = tsk.Sprite(puffin_sheet, 0, 200)
                    sprite_list.append(new_puffin)
                
    background.draw()
    for sprite in sprite_list:
        sprite.center_x += 0.2 * c.get_time()
        sprite.update(c.get_time())
        sprite.draw()
    pygame.display.flip()

    c.tick(30)