#!/usr/bin/env python3

from collections import defaultdict
from itertools import chain

def neighbours(x, y):
    yield x, y-1
    yield x, y+1
    yield x-1, y
    yield x+1, y

def checked_neighbours(x, y, xmax, ymax):
    for xi, yi in neighbours(x, y):
        if 0 <= xi < xmax and 0 <= yi < ymax:
            yield xi, yi

def find_start(m):
    for yi in range(len(m)):
        for xi in range(len(m[0])):
            if m[yi][xi] == '@':
                yield xi, yi

def get_keys(m):
    for yi in range(len(m)):
        for xi in range(len(m[0])):
            if m[yi][xi].islower():
                yield xi, yi

def find_path(m):

    ymax = len(m)
    xmax = len(m[0])

    pos = next(find_start(m))
    keys_collected = ()

    # queue contains (pos, keys_collected) tuple
    # where keys_collected is a sorted tuple
    d = [(pos, keys_collected)]

    # if pos in seen[keys_collected] then we have already been there
    seen = defaultdict(set)
    seen[keys_collected].add(pos)

    count_keys = sum(1 for _ in get_keys(m))

    steps_taken = 0

    while d:
        steps_taken += 1
        new_nodes = []
        for pos, keys in d:

            for xi, yi in checked_neighbours(*pos, xmax, ymax):

                # print("Considering {} {}".format(xi, yi))

                if m[yi][xi] == '#':
                    continue

                if m[yi][xi].isupper() and (not m[yi][xi].lower() in keys):
                    continue

                if m[yi][xi].islower():
                    new_keys = tuple(sorted(set(chain(keys, [m[yi][xi]]))))

                    if len(new_keys) == count_keys:
                        # print("Found shortest path:", steps_taken)
                        return steps_taken
                else:
                    new_keys = keys

                if (xi, yi) in seen[new_keys]:
                    continue

                seen[new_keys].add((xi, yi))
                new_nodes.append(((xi, yi), new_keys))

        d = new_nodes

        # print("steps:", steps_taken)

        # for i in d:
        #     print(i)
        # print("---")

def patch_for_part2(m):
    x, y = next(find_start(m))

    m[y-1] = "".join(chain(m[y-1][:x-1], "@#@", m[y-1][x+2:]))
    m[y  ] = "".join(chain(m[y  ][:x-1], "###", m[y  ][x+2:]))
    m[y+1] = "".join(chain(m[y+1][:x-1], "@#@", m[y+1][x+2:]))

    return m

def find_path_part2(m):

    ymax = len(m)
    xmax = len(m[0])

    index = 0
    all_pos = tuple(find_start(m))
    print(all_pos)
    n_robots = len(all_pos)
    keys_collected = ()

    # queue contains (index, pos, keys_collected) tuple
    # where keys_collected is a sorted tuple
    # and pos[index] is position of robot currently being controlled
    d = [(index, all_pos, keys_collected) for index in range(n_robots)]

    # if pos in seen[keys_collected] then we have already been there
    seen = defaultdict(set)
    seen[keys_collected].add(all_pos)

    count_keys = sum(1 for _ in get_keys(m))

    steps_taken = 0

    print(d)

    while d:
        steps_taken += 1
        new_nodes = []
        for index, all_pos, keys in d:

            for xi, yi in checked_neighbours(*all_pos[index], xmax, ymax):

                # print("Considering {} {}".format(xi, yi))

                if m[yi][xi] == '#':
                    continue

                if m[yi][xi].isupper() and (not m[yi][xi].lower() in keys):
                    continue

                new_pos = tuple(all_pos[i] if i != index else (xi, yi) for i in range(n_robots))

                if m[yi][xi].islower():
                    new_keys = tuple(sorted(set(chain(keys, [m[yi][xi]]))))

                    if len(new_keys) == count_keys:
                        print("Found shortest path:", steps_taken)
                        return steps_taken

                    if new_pos in seen[new_keys]:
                        continue

                    seen[new_keys].add(new_pos)
                    for i in range(n_robots):
                        new_nodes.append((i, new_pos, new_keys))

                else:
                    if new_pos in seen[keys]:
                        continue

                    seen[keys].add(new_pos)
                    new_nodes.append((index, new_pos, keys))

        d = new_nodes

        # print("steps:", steps_taken)

        # for i in d:
        #     print(i)
        # print("---")

if __name__=="__main__":
    with open("18_keys/input.txt", 'r') as f:
        m = [line.strip() for line in f]

    # Part 1
    print(find_path(m))

    patch_for_part2(m)

    for row in m:
        print(row)

    print(find_path_part2(m))
