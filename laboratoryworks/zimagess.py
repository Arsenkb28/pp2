import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("ARSEN")
icon = pygame.image.load('images/invincible.png')
pygame.display.set_icon(icon)

# Заполнение экрана белым цветом
screen.fill((255, 255, 255))
car_speed = 3
running = True
pygame.display.flip()

musics = pygame.mixer.Sound("song/metro.mp3")
musics.play(-1)
photo = pygame.image.load("images/korova.png")
players = pygame.image.load("images/player.png")

screen.blit(photo, ((0,0)))
screen.blit(players,((0,0)))

player_rect = players.get_rect()
player_rect.topleft = (0, 0)
pygame.display.update()
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  # Начальная позиция игрока
    keys= pygame.key.get_pressed()


    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= car_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += car_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= car_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += car_speed





    # Отображение фона и игрока
    screen.blit(photo, (0, 0))
    screen.blit(players, player_rect.topleft)
    pygame.display.update()

    # Обновление экрана
    pygame.display.flip()
clock.tick(20)
pygame.quit()



screen_width, screen_height = screen.get_size()
if player_rect.left > 0:  # Проверяем, что левая сторона не выходит за экран
    player_rect.x -= car_speed
if player_rect.right < screen_width:  # Проверяем, что правая сторона не выходит за экран
    player_rect.x += car_speed
if player_rect.top > 0:  # Проверяем, что верхняя сторона не выходит за экран
    player_rect.y -= car_speed
if player_rect.bottom < screen_height:  # Проверяем, что нижняя сторона не выходит за экран
    player_rect.y += car_speed
