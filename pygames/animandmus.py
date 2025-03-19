import pygame
import os
pygame.init()
running = True
screen = pygame.display.set_mode((600,720))
while running:





    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
