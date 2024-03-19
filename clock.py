import pygame
import sys
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

BACKGROUND = pygame.image.load('main-clock.png')
MINUTE_HAND = pygame.image.load('right-hand.png')
SECOND_HAND = pygame.image.load('left-hand.png')

def draw_clock():
    SCREEN.blit(BACKGROUND, (0, 0))

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((255, 255, 255))

        draw_clock()

        current_time = datetime.now()
        minute_angle = -current_time.minute * 6  
        second_angle = -current_time.second * 6 

        rotated_minute_hand = rotate_image(MINUTE_HAND, minute_angle)
        rotated_second_hand = rotate_image(SECOND_HAND, second_angle)

        SCREEN.blit(rotated_minute_hand, (WIDTH // 2 - rotated_minute_hand.get_width() // 2, HEIGHT // 2 - rotated_minute_hand.get_height() // 2))
        SCREEN.blit(rotated_second_hand, (WIDTH // 2 - rotated_second_hand.get_width() // 2, HEIGHT // 2 - rotated_second_hand.get_height() // 2))

        pygame.display.flip()

        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
