import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

paddle = pygame.Rect(350, 500, 150, 15)
paddle_speed = 7
ball_x = 400
ball_y = 400
ball_radius = 10

ball_dx = 4
ball_dy = 4

all_brickes = []
start_x = 40
start_y = 30


def create_bricks():
    for i in range(6):
        for j in range(8):
            br = pygame.Rect(start_x + j * 80 + j * 10, start_y + i * 30 + i * 10, 80, 30)
            all_brickes.append(br)


create_bricks()

f = pygame.font.SysFont("arial", 22)
score = 0
fail_counter = 0
game_paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed
    screen.fill("black")
    ball_x += ball_dx
    ball_y += ball_dy
    ball_rect = pygame.Rect(ball_x, ball_y, 2 * ball_radius, 2 * ball_radius)
    for br in all_brickes:
        pygame.draw.rect(screen, "orange", br)
        if br.colliderect(ball_rect):
            all_brickes.remove(br)
            ball_dy = abs(ball_dy)
            score += 1
    if ball_rect.colliderect(paddle):
        ball_dy = -ball_dy
    if ball_rect.right >= WIDTH:
        ball_dx = -abs(ball_dx)
    if ball_rect.left <= 0:
        ball_dx = abs(ball_dx)
    if ball_rect.top <= 0:
        ball_dy = abs(ball_dy)
    if ball_rect.top >= HEIGHT:
        game_paused = True
        fail_counter += 1
        while game_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_paused = False
                    running = False

                if event.type == pygame.KEYDOWN and fail_counter < 3:
                    if event.key == pygame.K_SPACE:
                        game_paused = False
                        ball_x = 400
                        ball_y = 300
                elif fail_counter > 3:
                    game_over_text = f.render("Game is Over", True, "red")
                    screen.blit(game_over_text, (400, 300))
                    print(fail_counter)
            pygame.draw.rect(screen, (70, 150, 225), paddle)
            pygame.display.update()
    score_text = f.render(f"Score : {score}", True, "white")
    screen.blit(score_text, (20,7))
    pygame.draw.circle(screen, "red", (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, (70, 150, 225), paddle)
    pygame.display.update()
    clock.tick(60)
