#!/usr/bin/env python3

from copy import deepcopy

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

if __name__=="__main__":
    with open("24_bugs/input.txt", 'r') as f:
        m = process(f.read())

    print(solve(m))
