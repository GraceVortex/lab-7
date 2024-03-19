import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
BALL_SIZE = BALL_RADIUS * 2
ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2

MOVE_SPEED= 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(0, ball_y - MOVE_SPEED)
            elif event.key == pygame.K_DOWN:
                ball_y = min(SCREEN_HEIGHT - BALL_SIZE, ball_y + MOVE_SPEED)
            elif event.key == pygame.K_LEFT:
                ball_x = max(0, ball_x - MOVE_SPEED)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(SCREEN_WIDTH - BALL_SIZE, ball_x + MOVE_SPEED)

    SCREEN.fill(WHITE)
    pygame.draw.circle(SCREEN, RED, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
