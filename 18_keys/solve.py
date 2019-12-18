#!/usr/bin/env python3

from itertools import chain
from heapq import *

def neighbours(x, y):
    # No need to check boundary since map is surrounded by walls
    yield x, y-1
    yield x, y+1
    yield x-1, y
    yield x+1, y

def get_keys(m, entrances):
    for yi in range(len(m)):
        for xi in range(len(m[0])):
            if m[yi][xi].islower() or m[yi][xi] in entrances:
                yield m[yi][xi], (xi, yi)

def find_path(m, k, pos):

    # queue contains (pos, requirements, keys_collected_so_far) tuple
    nodes = [(pos, "", k)]

    seen = set()
    seen.add(pos)

    distance = 0

    while nodes:
        distance += 1
        new_nodes = []
        for pos, req, collected in nodes:

            for xi, yi in neighbours(*pos):

                if m[yi][xi] == '#' or (xi, yi) in seen:
                    continue

                if m[yi][xi].islower():
                    new_coll = collected + m[yi][xi]
                    yield m[yi][xi], req, new_coll, distance
                else:
                    new_coll = collected

                if m[yi][xi].isupper():
                    new_req = req + m[yi][xi]
                else:
                    new_req = req

                seen.add((xi, yi))
                new_nodes.append(((xi, yi), new_req, new_coll))

        nodes = new_nodes

def get_graph_edges(m, entrances):

    edges = dict()

    for k1, starting_pos in get_keys(m, entrances):
        edges[k1] = dict()
        for k2, req, collected, distance in find_path(m, k1, starting_pos):
            edges[k1][k2] = (req, collected, distance)

    return edges

def find_start(m):
    for yi in range(len(m)):
        for xi in range(len(m[0])):
            if m[yi][xi] == '@':
                return (xi, yi)

def patch_for_part2(m):
    x, y = find_start(m)

    m[y-1] = "".join(chain(m[y-1][:x-1], "1#2", m[y-1][x+2:]))
    m[y  ] = "".join(chain(m[y  ][:x-1], "###", m[y  ][x+2:]))
    m[y+1] = "".join(chain(m[y+1][:x-1], "4#3", m[y+1][x+2:]))

    return m

def solve(m, entrances):
    edges = get_graph_edges(m, entrances)

    n_robots = len(entrances)
    n_keys = len(edges)

    # For part 2 we have 4 positions, but just one string of currently owned keys

    current = tuple(entrances)
    # heap contains distance, current_key and string of currently owned keys
    h = [(0, current, entrances)]

    # Distances uses current and sorted string owned as key
    distances = dict()
    distances[(current, entrances)] = 0

    while h:

        distance, current, owned = heappop(h)

        if distance > distances[(current, owned)]:
            continue

        if len(owned) == n_keys:
            return distance

        for index in range(n_robots):
            c = current[index]

            for other_key, (req, collected, d) in edges[c].items():

                if other_key in owned:
                    continue

                if any(r.lower() not in owned for r in req):
                    continue

                new_distance = distance + d
                new_current = tuple(
                    other_key if i == index else current[i] for i in range(n_robots)
                    )
                new_owned = "".join(sorted(set(owned + collected)))

                d_key = (new_current, new_owned)
                if (not d_key in distances) or new_distance < distances[d_key]:
                    heappush(h, (new_distance, new_current, new_owned))
                    distances[d_key] = new_distance

if __name__=="__main__":
    with open("18_keys/input.txt", 'r') as f:
        m = [line.strip() for line in f]

    print(solve(m, '@'))

    patch_for_part2(m)

    print(solve(m, '1234'))
