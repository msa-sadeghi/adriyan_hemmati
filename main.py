import pygame

pygame.init()

x,y = 400, 300
speed = 5
size = 50
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    screen.fill("pink")
    pygame.draw.rect(screen, (60, 200, 120), (x,y, size, size), border_radius=10)
    pygame.display.update()
    clock.tick(FPS)
