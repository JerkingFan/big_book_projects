import pygame
import random


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DVD")


x = random.randint(0, screen_width - 100)
y = random.randint(0, screen_height - 50)
speed_x = 3
speed_y = 3


font = pygame.font.SysFont(None, 74)
text = font.render('DVD', True, (255, 255, 255))
text_rect = text.get_rect()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    x += speed_x
    y += speed_y


    if x <= 0 or x + text_rect.width >= screen_width:
        speed_x = -speed_x
    if y <= 0 or y + text_rect.height >= screen_height:
        speed_y = -speed_y


    screen.fill((0, 0, 0))


    screen.blit(text, (x, y))


    pygame.display.flip()


    pygame.time.delay(10)


pygame.quit()
