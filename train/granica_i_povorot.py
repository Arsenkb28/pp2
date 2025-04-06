import pygame

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Настройки экрана
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("ARSEN")
icon = pygame.image.load('images/invincible.png')
pygame.display.set_icon(icon)

# Загрузка музыки
pygame.mixer.music.load("song/metro.mp3")
pygame.mixer.music.play(-1)  # Воспроизведение музыки в цикле

# Загрузка изображений
photo = pygame.image.load("images/korova.png")  # Фон
players = pygame.image.load("images/player.png")  # Машина

# Установка начальных параметров игрока
car_speed = 5
player_rect = players.get_rect()
player_rect.topleft = (0, 0)

# Угол поворота (по умолчанию 0 градусов, т.е. машина смотрит вправо)
rotation_angle = 0

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()

    # Движение игрока и изменение угла поворота
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= car_speed
        rotation_angle = 90  # Поворот на 90 градусов влево (машина смотрит влево)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += car_speed
        rotation_angle = -90  # Поворот на 90 градусов вправо (машина смотрит вправо)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= car_speed
        rotation_angle = 0  # Машина смотрит вверх (без поворота)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += car_speed
        rotation_angle = 180  # Поворот на 180 градусов (машина смотрит вниз)

    # Заполнение экрана белым цветом
    screen.fill((255, 255, 255))

    # Отображение фона
    screen.blit(photo, (0, 0))

    # Поворот изображения игрока в зависимости от угла
    rotated_player = pygame.transform.rotate(players, rotation_angle)

    # Центрирование машины после поворота (чтобы она не смещалась)
    rotated_rect = rotated_player.get_rect(center=player_rect.center)

    # Отображение повернутой машины
    screen.blit(rotated_player, rotated_rect.topleft)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)  # Установка 60 кадров в секунду

# Завершение работы Pygame
pygame.quit()
