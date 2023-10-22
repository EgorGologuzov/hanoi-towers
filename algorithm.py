

def execute_instruction(instruction, towers):
    for i in instruction:
        t1, t2 = towers[i[0]-1], towers[i[1]-1]
        t2.append(t1[-1])
        t1.pop(-1)
        yield False
    yield True


def algorithm(levels, start, finish):
    if (start == 1 and finish == 2) or (start == 2 and finish == 1):
        buffer = 3
    elif (start == 2 and finish == 3) or (start == 3 and finish == 2):
        buffer = 1
    else:
        buffer = 2

    if levels == 1:
        return [(start, finish)]
    else:
        return algorithm(levels - 1, start, buffer) + [(start, finish)] + algorithm(levels - 1, buffer, finish)


