import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

paddle_w, paddle_h = 15, 100
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
p1 = pygame.Rect(5, HEIGHT//2 - paddle_h//2, paddle_w, paddle_h)
p2 = pygame.Rect(WIDTH - 20, HEIGHT//2 - paddle_h//2, paddle_w, paddle_h)

paddle_speed = 10
ball_dx = 7 * random.choice((1, -1))
ball_dy = 7 * random.choice((1, -1))

p1_score = 0
p2_score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

run = True
while run:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and p1.top > 0:
        p1.y -= paddle_speed
    if keys[pygame.K_z] and p1.bottom < HEIGHT:
        p1.y += paddle_speed
    if keys[pygame.K_k] and p2.top > 0:
        p2.y -= paddle_speed
    if keys[pygame.K_m] and p2.bottom < HEIGHT:
        p2.y += paddle_speed

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_dx *= -1

    if ball.left <= 0:
        p2_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx = 7 * random.choice((1, -1))
        ball_dy = 7 * random.choice((1, -1))
    if ball.right >= WIDTH:
        p1_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx = 7 * random.choice((1, -1))
        ball_dy = 7 * random.choice((1, -1))

    pygame.draw.rect(screen, WHITE, p1)
    pygame.draw.rect(screen, WHITE, p2)
    pygame.draw.ellipse(screen, WHITE, ball)
    screen.blit(font.render(f"{p1_score}", True, WHITE), (WIDTH//2 - 40, 20))
    screen.blit(font.render(f"{p2_score}", True, WHITE), (WIDTH//2 + 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()