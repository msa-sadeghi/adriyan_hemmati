import pygame
pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

idle_images = []
for i in range(10):
    img = pygame.image.load(f"png/Idle/Idle__00{i}.png")
    img = pygame.transform.scale_by(img, 0.5)
    idle_images.append(img)

current_frame = 0
player_image = idle_images[current_frame]
player_rect = player_image.get_rect(topleft=(100, 300))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_image = idle_images[current_frame]
    current_frame += 1
    if current_frame >= len(idle_images):
        current_frame = 0
    screen.blit(player_image, player_rect)
    pygame.display.update()
    clock.tick(FPS)
