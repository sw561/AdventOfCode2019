#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop

def neighbours(x, y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def find_neighbouring_letter(s, x, y):
    for i, j in neighbours(x, y):
        if s[j][i].isalpha():
            return i, j

def get_portals(s):
    xmax = len(s[0])
    ymax = len(s)
    for j in range(ymax):
        for i in range(xmax):
            if s[j][i] != '.':
                continue

            temp = find_neighbouring_letter(s, i, j)

            if temp is None:
                continue

            a, b = temp
            c, d = find_neighbouring_letter(s, a, b)

            # Need to determine if portal is inwards or outwards.
            distance_dot_to_edge = min(i, xmax-i) + min(j, ymax-j)
            distance_letter_to_edge = min(a, xmax-a) + min(b, ymax-b)
            inwards = (distance_letter_to_edge < distance_dot_to_edge)

            if d < b or c < a:
                a, b, c, d = c, d, a, b

            yield (i, j), inwards, s[b][a] + s[d][c]

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
    for pos, inwards, labels in get_portals(s):
        label_pos[labels].append((pos, inwards))

    # print(label_pos)

    edges = defaultdict(dict)
    for label, f in label_pos.items():

        if len(f) == 2:
            ((pos1, i1), (pos2, i2)) = f
            edges[pos1][pos2] = (1, i2-i1)
            edges[pos2][pos1] = (1, i1-i2)

        for pos, inwards in f:
            for pos2, d in bfs(s, *pos):
                if pos != pos2:
                    edges[pos][pos2] = (d, 0)

    # for node, d in edges.items():
    #     print(node, d)

    return label_pos, edges

def solve(label_pos, edges, part2=False):

    # Do dijkstra from AA to ZZ
    pos = label_pos['AA'][0][0]
    destination = label_pos['ZZ'][0][0]

    # Heap contains distance, position, level
    h = [(0, pos, 0)]

    distances = dict()
    distances[(pos, 0)] = 0

    while h:
        distance, pos, level = heappop(h)

        if distance > distances[(pos, level)]:
            continue

        if pos == destination:
            if not part2 or level==0:
                return distance

        for n, (d, level_change) in edges[pos].items():
            new_distance = distance + d
            new_level = level + level_change

            if new_level < 0:
                continue

            if not ((n, new_level) in distances) or new_distance < distances[(n, new_level)]:
                heappush(h, (new_distance, n, new_level))
                distances[(n, new_level)] = new_distance

if __name__=="__main__":
    with open("20_donut/input.txt", 'r') as f:
        s = f.read().replace(' ', '#').split()

    label_pos, edges = process_input(s)
    print(solve(label_pos, edges))
    print(solve(label_pos, edges, part2=True))
