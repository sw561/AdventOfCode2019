#!/usr/bin/env python3

from itertools import chain
from collections import defaultdict
from heapq import heappush, heappop

def neighbours(x, y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def checked_neighbours(xmax, ymax, x, y):
    for xi, yi in neighbours(x, y):
        if 0 <= xi < xmax and 0 <= yi < ymax:
            yield xi, yi

def find_neighbouring_letter(s, xmax, ymax, x, y):
    for i, j in checked_neighbours(xmax, ymax, x, y):
        if s[j][i].isalpha():
            return i, j
    print(xmax, ymax, x, y)

def find_neighbouring_dot(s, xmax, ymax, x, y):
    x1, y1 = find_neighbouring_letter(s, xmax, ymax, x, y)
    for i, j in chain(
            checked_neighbours(xmax, ymax, x, y),
            checked_neighbours(xmax, ymax, x1, y1)
            ):
        if s[j][i] == '.':
            return i, j
    print(s)
    print(xmax, ymax, x, y)

def get_portals(s):
    xmax = len(s[0])
    ymax = len(s)
    for j in range(ymax):
        for i in range(xmax):
            if s[j][i].isalpha():
                x, y = find_neighbouring_dot(s, xmax, ymax, i, j)
                a, b = find_neighbouring_letter(s, xmax, ymax, x, y)
                c, d = find_neighbouring_letter(s, xmax, ymax, a, b)
                if d < b or c < a:
                    a, b, c, d = c, d, a, b
                yield x, y, s[b][a] + s[d][c]

def bfs(s, x, y):
    pos = (x, y)
    seen = set([pos])
    distance = 0

    nodes = [pos]
    while nodes:
        new_nodes = []
        for pos in nodes:
            for x, y in neighbours(*pos):
                if (x, y) in seen:
                    continue

                if s[y][x] == '.':
                    new_nodes.append((x, y))
                    seen.add((x, y))
                elif s[y][x].isalpha():
                    yield pos, distance

        nodes = new_nodes
        distance += 1

def process_input(s):
    label_pos = defaultdict(list)
    for x, y, labels in set(get_portals(s)):
        label_pos[labels].append((x, y))

    # print(label_pos)

    edges = defaultdict(dict)
    for label, f in label_pos.items():

        if len(f) == 2:
            edges[f[0]][f[1]] = 1
            edges[f[1]][f[0]] = 1

        for pos in f:
            for pos2, d in bfs(s, *pos):
                if pos != pos2:
                    edges[pos][pos2] = d

    # for node, d in edges.items():
    #     print(node, d)

    return label_pos, edges

def solve(s):
    label_pos, edges = process_input(s)
    # print("--")

    # Do dijkstra from AA to ZZ
    pos = label_pos['AA'][0]
    destination = label_pos['ZZ'][0]

    # Heap contains distance, position
    h = [(0, pos)]

    distances = dict()
    distances[pos] = 0

    while h:
        distance, pos = heappop(h)

        if distance > distances[pos]:
            continue

        if pos == destination:
            return distance

        for n, d in edges[pos].items():
            new_distance = distance + d

            if not (n in distances) or new_distance < distances[n]:
                heappush(h, (new_distance, n))
                distances[n] = new_distance

        # print(h)

if __name__=="__main__":
    with open("20_donut/input.txt", 'r') as f:
        s = f.read().replace(' ', '#').split()

    print(solve(s))
