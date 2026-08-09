import pygame
import random

pygame.init()

WIDTH = 1024
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
clock = pygame.time.Clock()

player = pygame.Rect(50, 400, 50, 50)
all_coins = []
for i in range(5):
    x = random.randint(100, 900)
    y = random.randint(100, 500)
    coin = pygame.Rect(x, y, 25, 25)
    all_coins.append(coin)

vel_x = 4
vel_y = 3
FRICTION = 0.9
MAX_SPEED = 8
ACCEL = 0.5
GRAVITY = 0.5
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vel_x -= ACCEL
    if keys[pygame.K_RIGHT]:
        vel_x += ACCEL
    if player.left <= 0 or player.right >= WIDTH:
        vel_x *= -1
    if keys[pygame.K_UP]:
        vel_y -= ACCEL
    if keys[pygame.K_DOWN]:
        vel_y += ACCEL
    if keys[pygame.K_SPACE]:
        vel_y = -12
    vel_x = max(-MAX_SPEED, min(MAX_SPEED, vel_x))
    vel_y = max(-MAX_SPEED, min(MAX_SPEED, vel_y))
    vel_x *= FRICTION
    vel_y *= FRICTION
    vel_y += GRAVITY

    if player.bottom + vel_y >= HEIGHT:
        vel_y = 0
        # GRAVITY = 0

    player.x += vel_x
    player.y += vel_y
    screen.fill("gray")
    for c in all_coins:
        pygame.draw.ellipse(screen, "gold", c)
    pygame.draw.rect(screen, "green", player)
    pygame.display.update()
    clock.tick(FPS)
