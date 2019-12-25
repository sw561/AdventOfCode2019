#!/usr/bin/env python3

from copy import copy
from collections import defaultdict

def neighbours(x, y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def checked_neighbours(x, y, xmax, ymax):
    for i, j in neighbours(x, y):
        if 0 <= i < xmax and 0 <= j < ymax:
            yield 0, i, j

part1_neighbours = {(x, y): list(checked_neighbours(x, y, 5, 5))
    for x in range(5) for y in range(5)}

def recursive_neighbours(level, x, y, xmax, ymax):
    for i, j in neighbours(x, y):
        if i < 0:
            yield level-1, 1, 2
        elif i == xmax:
            yield level-1, 3, 2
        elif j < 0:
            yield level-1, 2, 1
        elif j == ymax:
            yield level-1, 2, 3
        elif i == 2 and j == 2:
            # Go to next level
            if x == 1:
                for yy in range(5):
                    yield level+1, 0, yy
            elif x == 3:
                for yy in range(5):
                    yield level+1, 4, yy
            elif y == 1:
                for xx in range(5):
                    yield level+1, xx, 0
            elif y == 3:
                for xx in range(5):
                    yield level+1, xx, 4
        else:
            yield level, i, j

part2_neighbours = {(x, y): list(recursive_neighbours(0, x, y, 5, 5))
    for x in range(5) for y in range(5)}

def process(s):
    d = set()
    s = s.split()
    for y in range(5):
        for x in range(5):
            if s[y][x] == '#':
                d.add((0, x, y))

    return d

def update(d, part2=False):
    if not part2:
        neighbours = part1_neighbours
    else:
        neighbours = part2_neighbours
    count = defaultdict(int)

    for (level, x, y) in d:
        for dl, i, j in neighbours[(x, y)]:
            count[(level+dl, i, j)] += 1

    new_d = set()

    for square, c in count.items():
        if c == 1:
            new_d.add(square)
        elif c == 2 and square not in d:
            new_d.add(square)
    return new_d

def biodiversity(d):
    b = 0
    for (level, x, y) in d:
        b |= (1 << (y*5 + x))
    return b

def solve(d):
    seen = set()
    seen.add(biodiversity(d))
    while True:
        d = update(d)
        b = biodiversity(d)
        if b in seen:
            return b
        else:
            seen.add(b)

def solve_part2(d, n=200):
    for _ in range(n):
        d = update(d, part2=True)

    return len(d)

if __name__=="__main__":
    with open("24_bugs/input.txt", 'r') as f:
        d = process(f.read())

    print(solve(copy(d)))

    print(solve_part2(d))
