import math
from collections import deque

f = open('input.txt', 'r')
line = f.readlines()
f.close()


def window(seq, n=4):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield list(win)
    append = win.append

    for e in it:
        append(e)
        yield list(win)


window(line[0], 4)

    