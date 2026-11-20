import pygame

pygame.init()
import random

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
x = 300
y = 300
size = 20
snake = [(x, y)]
dx = 0
dy = 0
food_x = random.randrange(0, 600, size)
food_y = random.randrange(0, 600, size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -size
                dy = 0
            if event.key == pygame.K_RIGHT:
                dx = size
                dy = 0
            if event.key == pygame.K_UP:
                dx = 0
                dy = -size
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = size
    x += dx
    y += dy
    snake.insert(0, (x, y))
    if (x,y) in snake[2:]:
        running = False
    if x == food_x and y == food_y:
        food_x = random.randrange(0, 600, size)
        food_y = random.randrange(0, 600, size)
    else:
        snake.pop()
    screen.fill("white")
    pygame.draw.rect(screen, "red", (food_x, food_y, size, size))
    for part in snake:
        pygame.draw.rect(screen, "green", (part[0], part[1], size, size))
    pygame.display.update()
    clock.tick(10)
