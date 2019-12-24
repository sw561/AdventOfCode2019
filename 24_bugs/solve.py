#!/usr/bin/env python3

from copy import deepcopy
from collections import defaultdict

def neighbours(x, y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def checked_neighbours(x, y, xmax, ymax):
    for i, j in neighbours(x, y):
        if 0 <= i < xmax and 0 <= j < ymax:
            yield i, j

def update(m, m2):
    xmax = len(m[0])
    ymax = len(m)

    for y in range(ymax):
        for x in range(xmax):

            live = sum(m[j][i] == '#' for i, j in checked_neighbours(x, y, xmax, ymax))

            if m[y][x] == '#' and live != 1:
                m2[y][x] = '.'
            elif m[y][x] == '.' and 1 <= live <= 2:
                m2[y][x] = '#'
            else:
                m2[y][x] = m[y][x]

def process(s):
    return [[c for c in line.strip()] for line in s.split()]

def display(m):
    print("\n".join("".join(row) for row in m))

def iter_m(m):
    for row in m:
        for c in row:
            yield c

def biodiversity(m):
    b = 0
    for i, c in enumerate(iter_m(m)):
        if c == '#':
            b |= (1 << i)
    return b

def solve(m):
    m = deepcopy(m)
    m2 = deepcopy(m)
    seen = set()
    seen.add(biodiversity(m))
    while True:
        update(m, m2)
        m2, m = m, m2
        b = biodiversity(m)
        if b in seen:
            # display(m)
            return b
        else:
            seen.add(b)

def part2_neighbours(level, x, y, xmax, ymax):
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

def display_part2(d):
    for i in sorted(d.keys()):
        print(i)
        display(d[i])
        print("------------")

def update_part2(d, d2):
    xmax = len(d[0][0])
    ymax = len(d[0])

    dkeys = list(d.keys())
    for level in range(min(dkeys)-1, max(dkeys)+2):
        for y in range(ymax):
            for x in range(xmax):
                if x == 2 and y == 2:
                    continue
                live = sum(d[l][j][i] == '#' for l, i, j in part2_neighbours(level, x, y, xmax, ymax))

                if d[level][y][x] == '#' and live != 1:
                    d2[level][y][x] = '.'
                elif d[level][y][x] == '.' and 1 <= live <= 2:
                    d2[level][y][x] = '#'
                else:
                    d2[level][y][x] = d[level][y][x]

    for level in list(d2.keys()):
        if biodiversity(d2[level]) == 0:
            del d2[level]
    for level in list(d.keys()):
        if biodiversity(d[level]) == 0:
            del d[level]

def solve_part2(m, n=200):
    d = defaultdict(lambda: [['.']*5 for _ in range(5)])
    d2 = deepcopy(d)

    d[0] = m

    # display_part2(d)

    for _ in range(n):
        update_part2(d, d2)
        d2, d = d, d2

    # display_part2(d)

    return count_bugs(d)

def count_bugs(d):
    s = 0
    for level in d.keys():
        for row in d[level]:
            for c in row:
                if c == '#':
                    s += 1
    return s

if __name__=="__main__":
    with open("24_bugs/input.txt", 'r') as f:
        m = process(f.read())

    print(solve(m))

    d = solve_part2(m)

    print(d)
