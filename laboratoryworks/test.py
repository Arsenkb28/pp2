import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("ARSEN")
icon = pygame.image.load('images/invincible.png')
pygame.display.set_icon(icon)

# Заполнение экрана белым цветом
screen.fill((255, 255, 255))



car_speed = 5
car_x = 150


running = True
pygame.display.flip()

musics = pygame.mixer.Sound("song/metro.mp3")
musics.play(-1)
photo = pygame.image.load("images/korova.png")
players = pygame.image.load("images/player.png")

screen.blit(photo, ((0,0)))
screen.blit(players,((150,0)))


while running:
    # Обработка событий

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill((49, 25, 26))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    elif keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Обновление экрана
    pygame.display.flip()
clock.tick(20)
pygame.quit()
