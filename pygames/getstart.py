import pygame
import os
pygame.init()
screen = pygame.display.set_mode((1200,1200))

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

'''
square = pygame.Surface((50,150))
square.fill(("Blue"))


'''
photo = pygame.image.load('images/icon.png')
running = True
while running:

#    pygame.draw.circle(screen, 'Red', ((150,150)), 75)
#    screen.blit(square,(10,0))

    screen.blit(photo,(100,100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

# НАЖАТИЕ КНОПОК
# в ЦИКЛЕ
'''
elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_a:
        screen.fill((70,44,133))
'''