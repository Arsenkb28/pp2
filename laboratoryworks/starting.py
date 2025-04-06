import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("ARSEN")
icon = pygame.image.load('images/invincible.png')
pygame.display.set_icon(icon)

# Заполнение экрана белым цветом
screen.fill((255, 255, 255))

# Создание прямоугольника
square = pygame.Surface((200, 100))
square.fill((111, 111, 111))

# Отображение квадрата на экране
screen.blit(square, (50, 50))

# Рисование круга на квадрате
pygame.draw.circle(square, (209, 10, 10), (100, 50), 15)

running = True
pygame.display.flip()

#text
myfont = pygame.font.Font(None,20)
text = myfont.render("Hello, Pygame!", True, (0, 128, 255))
text_rect = text.get_rect(center=(300, 150))
screen.blit(text, text_rect)
#text
photo = pygame.image.load("images/invincible.png")
screen.blit(photo, ((20,20)))
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill((49, 25, 26))  # Заполнение экрана другим цветом

    # Отображение квадрата на экране после событий
    screen.blit(square, (50, 50))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
