import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont("Arial", 40)

bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.5
jump_strength = -7

pipe_width = 70
pipe_gap = 300
pipe_color = GREEN
pipes = []
pipe_speed = 3
lives = 3
invincible = False
invincible_timer = 0
def create_pipe():
    y = random.randint(200, 800)
    return {"top": y - pipe_gap // 2, "bottom": y + pipe_gap // 2, "x": WIDTH}
pipes.append(create_pipe())
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    bird_velocity += gravity
    bird_y += bird_velocity

    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    for pipe in pipes:
        pipe['x'] -= pipe_speed
        pygame.draw.rect(screen, pipe_color, (pipe['x'], 0, pipe_width, pipe['top']))
        pygame.draw.rect(screen, pipe_color, (pipe['x'], pipe['bottom'], pipe_width, HEIGHT - pipe['bottom']))

    if pipes[-1]['x'] < WIDTH - 400:  # ⬅️ WIDER between pipes
        pipes.append(create_pipe())

    if pipes[0]['x'] < -pipe_width:
        pipes.pop(0)

    if not invincible:
        for pipe in pipes:
            if pipe['x'] < bird_x < pipe['x'] + pipe_width:
                if bird_y - bird_radius < pipe['top'] or bird_y + bird_radius > pipe['bottom']:
                    lives -= 1
                    invincible = True
                    invincible_timer = pygame.time.get_ticks()
                    bird_y = HEIGHT // 2
                    bird_velocity = 0
                    break

        if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
            lives -= 1
            invincible = True
            invincible_timer = pygame.time.get_ticks()
            bird_y = HEIGHT // 2
            bird_velocity = 0

    if invincible and pygame.time.get_ticks() - invincible_timer > 2000:
        invincible = False

    lives_text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(lives_text, (10, 10))

    if lives <= 0:
        running = False

    pygame.display.update()

pygame.quit()
sys.exit()