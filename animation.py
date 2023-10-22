import pygame as pg


def draw(screen, towers, root):
    screen.fill((255, 255, 255))
    for t_num in range(len(towers)):
        for l_num in range(len(towers[t_num])):
            compression = 3*towers[t_num][l_num]
            x, y = (130 * t_num + 10) + compression, 12 * l_num + 2
            pg.draw.rect(screen, (0, 0, 0), (x, y, 120 - 2 * compression, 10))
    root.blit(pg.transform.flip(screen, False, True), (0, 0))


def init(levels, start, towers):
    # max 20 levels in tower
    start -= 1
    # инициализирует значения ширины этажей начальной башни
    for i in range(levels):
        towers[start].append(i)

