import pygame
from random import randint

dis = pygame.display.set_mode((700, 700))

x, y = randint(350, 500), randint(200, 400)
count = 0

clock = pygame.time.Clock()
FPS = 1000

def random_side(side):
    if side == 1:
        return (350, 100)
    elif side == 2:
        return (600, 500)
    return (100, 500)

pygame.draw.line(dis, (255, 255, 255), (350, 100), (600, 500))
pygame.draw.line(dis, (255, 255, 255), (350, 100), (100, 500))
pygame.draw.line(dis, (255, 255, 255), (600, 500), (100, 500))

while True:
    pygame.display.set_caption(f'Count: {count}, FPS:{clock.get_fps()//1}')
    side = random_side(randint(1, 3))
    x, y = (side[0] + x) / 2, (side[1] + y) / 2
    count += 1
    clock.tick(FPS)

    pygame.draw.rect(dis, (255,255,255), (x, y, 1, 1))

    pygame.display.update()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit()