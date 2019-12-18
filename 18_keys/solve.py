#!/usr/bin/env python3

from itertools import chain
from heapq import *

def neighbours(x, y):
    # No need to check boundary since map is surrounded by walls
    yield x, y-1
    yield x, y+1
    yield x-1, y
    yield x+1, y

def get_keys(m, entrances='@'):
    for yi in range(len(m)):
        for xi in range(len(m[0])):
            if m[yi][xi].islower() or m[yi][xi] in entrances:
                yield m[yi][xi], (xi, yi)

def find_path(m, k, pos):

    # queue contains (pos, requirements, keys_collected_so_far) tuple
    # where keys_collected is a sorted tuple
    d = [(pos, "", k)]

    seen = set()
    seen.add(pos)

    steps_taken = 0

    while d:
        steps_taken += 1
        new_nodes = []
        for pos, requirements, keys_collected in d:

            for xi, yi in neighbours(*pos):

                # print("Considering {} {}".format(xi, yi))

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

        # print("steps:", steps_taken)

        # for i in d:
        #     print(i)
        # print("---")

def get_graph_edges(m, entrances='@'):

    # edges[(i, j)] is list of keys required to go from key i to key j
    # i < j always
    edges = dict()

    for k, starting_pos in get_keys(m, entrances=entrances):
        edges[k] = dict()
        for other_key, requirements, keys_collected, distance in find_path(m, k, starting_pos):
            edges[k][other_key] = (requirements, keys_collected, distance)

    return edges

def solve(m):
    edges = get_graph_edges(m)

    n_keys = len(edges)

    # for k in sorted(edges.keys()):
    #     for k2, (r, d) in edges[k].items():
    #         print((k, k2), r, d)
    # print("-------------")

    # Now do dijkstra starting at '@' and moving until all keys are collected,
    # but only considering edges which are available (no requirements)

    start_key = '@'
    # heap contains distance current_key and string of currently owned keys
    h = [(0, start_key, start_key)]

    # Distances uses current_key and sorted string owned_keys as key
    distances = dict()
    distances[(start_key, start_key)] = 0

    # print(h)
    # print(distances)
    while h:

        current_distance, current_key, owned_keys = heappop(h)

        if current_distance > distances[(current_key, owned_keys)]:
            continue

        if len(owned_keys) == n_keys:
            # print("Found shortest route", current_distance)
            return current_distance

        for other_key in edges[current_key].keys():

            if other_key in owned_keys:
                continue

            requirements, keys_collected, distance = edges[current_key][other_key]
            if any(r.lower() not in owned_keys for r in requirements):
                continue

            new_distance = current_distance + distance
            new_owned_keys = "".join(sorted(set(owned_keys + keys_collected)))
            if (other_key, new_owned_keys) in distances and distances[(other_key, new_owned_keys)] <= new_distance:
                continue
            else:
                heappush(h, (new_distance, other_key, new_owned_keys))
                distances[(other_key, new_owned_keys)] = new_distance

        # print("--")
        # for d, k, o in h:
        #     print(d, k, "".join(x for x in sorted(o)))
        # print(distances)

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

def solve_part2(m):
    edges = get_graph_edges(m, entrances='1234')

    n_keys = len(edges)

    # for k in sorted(edges.keys()):
    #     for k2, (r, d) in edges[k].items():
    #         print((k, k2), r, d)
    # print("-------------")

    # For part 2 we have 4 positions, but just one string of currently owned keys

    current = ('1', '2', '3', '4')
    owned = '1234'
    # heap contains distance current_key and string of currently owned keys
    h = [(0, current, owned)]

    # Distances uses current_key and sorted string owned_keys as key
    distances = dict()
    distances[(current, owned)] = 0

    # print(h)
    # print(distances)
    while h:

        current_distance, current_keys, owned_keys = heappop(h)

        if current_distance > distances[(current_keys, owned_keys)]:
            continue

        if len(owned_keys) == n_keys:
            # print("Found shortest route", current_distance)
            return current_distance

        for index in range(4):
            current_key = current_keys[index]

            for other_key in edges[current_key].keys():

                if other_key in owned_keys:
                    continue

                requirements, keys_collected, distance = edges[current_key][other_key]
                if any(r.lower() not in owned_keys for r in requirements):
                    continue

                new_distance = current_distance + distance
                new_current_keys = tuple(other_key if i == index else current_keys[i] for i in range(4))
                new_owned_keys = "".join(sorted(set(owned_keys + keys_collected)))

                if (new_current_keys, new_owned_keys) in distances and distances[(new_current_keys, new_owned_keys)] <= new_distance:
                    continue
                else:
                    heappush(h, (new_distance, new_current_keys, new_owned_keys))
                    distances[(new_current_keys, new_owned_keys)] = new_distance

        # print("--")
        # for d, k, o in h:
        #     print(d, "".join(k), "".join(x for x in sorted(o)))
        # print(distances)
        # input()

if __name__=="__main__":
    with open("18_keys/input.txt", 'r') as f:
        m = [line.strip() for line in f]

    # Part 1
    print(solve(m))

    patch_for_part2(m)

    # for row in m:
    #     print(row)

    print(solve_part2(m))
