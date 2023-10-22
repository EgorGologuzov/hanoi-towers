from animation import *
from algorithm import *


def main():
    l = int(input('Input levels number: '))
    s = int(input('Input start position: '))
    f = int(input('Input finish position: '))

    pg.init()
    w, h = 400, 242
    root = pg.display.set_mode((w, h))
    clock = pg.time.Clock()
    screen = pg.Surface((400, 242))
    towers = [[], [], []]
    instruction = algorithm(l, s, f)

    init(l, s, towers)
    run = True
    step = execute_instruction(instruction, towers)
    while run:
        clock.tick(10)
        draw(screen, towers, root)
        if next(step):
            run = False
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False


if __name__ == '__main__':
    main()


