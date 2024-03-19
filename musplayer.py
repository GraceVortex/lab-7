import pygame
import os

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Music Player")

MUSIC_DIR = "C:/Users/User/Desktop/mbdtf"
music_files = os.listdir(MUSIC_DIR)
current_track_index = 0

current_track = pygame.mixer.Sound(os.path.join(MUSIC_DIR, music_files[current_track_index]))

def play_track():
    pygame.mixer.music.load(os.path.join(MUSIC_DIR, music_files[current_track_index]))
    pygame.mixer.music.play()

running = True
playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_track_index = (current_track_index + 1) % len(music_files)
                play_track()
            elif event.key == pygame.K_LEFT:
                current_track_index = (current_track_index - 1) % len(music_files)
                play_track()

pygame.quit()
