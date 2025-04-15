import os
import pygame
import json
import psycopg2
from game_objects import Player, Food, Wall

# Connect to PostgreSQL
conn = psycopg2.connect(database="mydatabase",
                        user="postgres",
                        host='localhost',
                        password="1234",
                        port=5432)
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(25) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    level INTEGER NOT NULL DEFAULT 1,
    score INTEGER NOT NULL DEFAULT 0,
    paused_state TEXT
);
""")
conn.commit()

# Load colors
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'color.json')
with open(file_path) as f:
    color = json.loads(f.read())

# Ask for username
username = input("Enter your username: ")

# Get or create user
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()
if user:
    user_id = user[0]
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()

# Get progress
cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
data = cur.fetchone()
if data:
    LEVEL, BALANCE = data
else:
    LEVEL, BALANCE = 1, 0
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, LEVEL, BALANCE))
    conn.commit()

# Game setup
pygame.init()
h = w = 400
win = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake')

def add_transparent_text(main_surface, text, size, x, y):
    font = pygame.font.SysFont('comicsansms', size)
    text = font.render(text, True, color['text'])
    surface = pygame.Surface((w, h))
    surface.fill(color['bg_color'])
    surface.blit(text, (0, 0))
    surface.set_alpha(150)
    main_surface.blit(surface, (x, y))

def fill_background(surface, level, balance, n_to_next_lvl):
    surface.fill(color['bg_color'])
    add_transparent_text(surface, f'LVL: {level}', 35, 0, 0)
    add_transparent_text(surface, f'Need: {balance}/{n_to_next_lvl}', 35, 200, 0)
    for i in range(0, w, 20):
        pygame.draw.line(surface, color['black'], (0, max(i - 1, 0)), (w, max(i - 1, 0)), 2)
        pygame.draw.line(surface, color['black'], (max(i - 1, 0), 0), (max(i - 1, 0), h), 2)

fill_background(win, LEVEL, BALANCE, 5)

wall = Wall(level=LEVEL)
player = Player(wall.points)
food = Food(player.points + wall.points)
speed = 5 if LEVEL <= 3 else 11
N_to_next_lvl = 5 if LEVEL <= 3 else 999
clock = pygame.time.Clock()
run = True
losed = None
paused = False

while run:
    k_down_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            k_down_events.append(event)
            if event.key == pygame.K_p:  # Pause
                paused = not paused
                if paused:
                    state = {
                        "level": LEVEL,
                        "score": BALANCE
                    }
                    cur.execute("""
                        UPDATE user_score SET level = %s, score = %s, paused_state = %s
                        WHERE user_id = %s
                    """, (LEVEL, BALANCE, json.dumps(state), user_id))
                    conn.commit()
            if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and losed is not None:
                wall = Wall(level=LEVEL)
                player = Player(wall.points)
                food = Food(player.points + wall.points)
                BALANCE = 0
                losed = None

    if not paused and losed is None:
        player.process_input(k_down_events)
        fill_background(win, LEVEL, BALANCE, N_to_next_lvl)
        bumped_to_wall = wall.can_go(player.points[0], player.dx, player.dy)
        if bumped_to_wall:
            losed = bumped_to_wall
        if losed is None:
            losed = player.move(w, h)
        eat_food = food.can_eat(player.points[0])
        if eat_food:
            player.add(player.points[0])
            BALANCE += 1
            if BALANCE == N_to_next_lvl:
                LEVEL += 1
                wall = Wall(LEVEL)
                player = Player(wall.points)
                if LEVEL <= 3:
                    speed += 2
                else:
                    speed += 8
                    N_to_next_lvl = 999
                BALANCE = 0
            food.change_pos(food.points + player.points + wall.points)
        player.draw(win)
        food.draw(win)
        wall.draw(win)

    elif losed:
        start = [player.points[0].x, player.points[0].y]
        end = list(start)
        if losed == 'down_collide':
            end[0] += 20
            end[1] += 18
            start[1] += 18
        elif losed == 'up_collide':
            end[0] += 20
        elif losed == 'left_collide':
            end[1] += 20
        elif losed == 'right_collide':
            start[0] += 18
            end[0] += 18
            end[1] += 20
        pygame.draw.line(win, color['red'], start, end, 2)
        font = pygame.font.SysFont('comicsansms', 80)
        text = font.render('You Lose', True, color['red'])
        win.blit(text, (30, 120))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
print(losed)

cur.close()
conn.close()