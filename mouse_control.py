import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ماوس")
clock = pygame.time.Clock()
font  = pygame.font.SysFont('Arial', 28)
circles = []   # لیست دایره‌های کشیده‌شده
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # کلیک ماوس — یک‌بار در لحظه کلیک
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:    # کلیک چپ
                circles.append(event.pos)
            if event.button == 3:    # کلیک راست
                circles.clear()
    # موقعیت لحظه‌ای ماوس
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # وضعیت لحظه‌ای دکمه‌ها (چپ، وسط، راست)
    left, middle, right = pygame.mouse.get_pressed()
    screen.fill((25, 25, 35))
   # رسم همه دایره‌های ثبت‌شده
    for pos in circles:
        pygame.draw.circle(screen, (100,200,255), pos, 20)
    # دایره دنبال‌کننده ماوس
    color = (255,100,100) if left else (100,255,150)
    pygame.draw.circle(screen, color, (mouse_x, mouse_y), 10)
    # نمایش مختصات
    pos_text = font.render(f'({mouse_x}, {mouse_y})', True, (255,255,255))
    screen.blit(pos_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
