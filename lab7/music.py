import pygame
import os

pygame.init()
pygame.mixer.init()

music_dir = r"C:\Users\admin\PycharmProjects\pp2\lab7\musica"  # folder with musics
songs = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
idx = 0  # current song

img = pygame.image.load('img.png')
W, H = img.get_size()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music Player")


def play_song():  # to play
    pygame.mixer.music.load(os.path.join(music_dir, songs[idx]))
    pygame.mixer.music.play()


if songs:
    play_song()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # pause or play -> space
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # stop -> S
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:  # next
                idx = (idx + 1) % len(songs)
                play_song()
            elif event.key == pygame.K_LEFT:  # previous
                idx = (idx - 1) % len(songs)
                play_song()

    screen.blit(img, (0, 0))
    pygame.display.flip()

pygame.quit()