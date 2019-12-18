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
    d = [(pos, "", k)]

    seen = set()
    seen.add(pos)

    steps_taken = 0

    while d:
        steps_taken += 1
        new_nodes = []
        for pos, requirements, keys_collected in d:

            for xi, yi in neighbours(*pos):

                if m[yi][xi] == '#':
                    continue

                if (xi, yi) in seen:
                    continue

                if m[yi][xi].islower():
                    new_keys = keys_collected + m[yi][xi]
                    yield m[yi][xi], requirements, new_keys, steps_taken
                else:
                    new_keys = keys_collected

                if m[yi][xi].isupper():
                    new_requirements = requirements + m[yi][xi]
                else:
                    new_requirements = requirements

                seen.add((xi, yi))
                new_nodes.append(((xi, yi), new_requirements, new_keys))

        d = new_nodes

def get_graph_edges(m, entrances):

    edges = dict()

    for k, starting_pos in get_keys(m, entrances):
        edges[k] = dict()
        for other_key, requirements, keys_collected, distance in find_path(m, k, starting_pos):
            edges[k][other_key] = (requirements, keys_collected, distance)

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

    n_keys = len(edges)

    # For part 2 we have 4 positions, but just one string of currently owned keys

    current = tuple(entrances)
    # heap contains distance current_key and string of currently owned keys
    h = [(0, current, entrances)]

    # Distances uses current_key and sorted string owned_keys as key
    distances = dict()
    distances[(current, entrances)] = 0

    while h:

        current_distance, current_keys, owned_keys = heappop(h)

        if current_distance > distances[(current_keys, owned_keys)]:
            continue

        if len(owned_keys) == n_keys:
            return current_distance

        for index in range(len(entrances)):
            current_key = current_keys[index]

            for other_key, (requirements, keys_collected, distance) in edges[current_key].items():

                if other_key in owned_keys:
                    continue

                if any(r.lower() not in owned_keys for r in requirements):
                    continue

                new_distance = current_distance + distance
                new_current_keys = tuple(other_key if i == index else current_keys[i] for i in range(len(entrances)))
                new_owned_keys = "".join(sorted(set(owned_keys + keys_collected)))

                if (new_current_keys, new_owned_keys) in distances and distances[(new_current_keys, new_owned_keys)] <= new_distance:
                    continue
                else:
                    heappush(h, (new_distance, new_current_keys, new_owned_keys))
                    distances[(new_current_keys, new_owned_keys)] = new_distance

if __name__=="__main__":
    with open("18_keys/input.txt", 'r') as f:
        m = [line.strip() for line in f]

    print(solve(m, '@'))

    patch_for_part2(m)

    print(solve(m, '1234'))
