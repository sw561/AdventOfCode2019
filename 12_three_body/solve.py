#!/usr/bin/env python3

import re

def process_input(f):
    r = re.compile(r'-?\d+')
    positions = []
    for line in f:
        m = r.findall(line)
        positions.append([[int(x) for x in m], [0, 0, 0]])
    return positions

def v_diff(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def pe(pos):
    return sum(abs(pos[0][d_index]) for d_index in range(3))

def ke(pos):
    return sum(abs(pos[1][d_index]) for d_index in range(3))

def energy(positions):
    e = 0
    for i in range(len(positions)):
        # pe = sum(abs(positions[i][0][d_index]) for d_index in range(3))
        # ke = sum(abs(positions[i][1][d_index]) for d_index in range(3))
        # e += pe * ke
        e += pe(positions[i]) * ke(positions[i])
    return e

def hashable(positions):
    return tuple(map(tuple, (map(tuple, x) for x in positions)))

def easy_hash(positions):
    peke = tuple(sorted((pe(pos), ke(pos)) for pos in positions))
    return peke

def simulate(positions, t_part1=1000):

    part1 = None
    part2 = None

    seen = dict()
    seen[hashable(positions)] = 0

    t = 0
    while (part1 is None or part2 is None):
        t += 1
        
        # Update velocities first
        for i in range(len(positions)):
            for d_index in range(3):
                positions[i][1][d_index] += sum(
                    v_diff(positions[j][0][d_index], positions[i][0][d_index])\
                    for j in range(len(positions)) if j != i)

        # Now update positions
        for i in range(len(positions)):
            for d_index in range(3):
                positions[i][0][d_index] += positions[i][1][d_index]

        h = hashable(positions)
        if h in seen:
            print("Found reoccurence from {} to {}".format(seen[h], t))
            part2 = t
        else:
            seen[h] = t

        if t == t_part1:
            part1 = energy(positions)
            print("Part 1 done", part1)

        if not t%10000:
            print(t)

    return part1, part2

def print_routine(positions):
    print("---")
    for posv in positions:
        pos = posv[0]
        v = posv[1]
        print("pos=<x={:3d}, y={:3d}, z={:3d}>, vel=<x={:3d}, y={:3d}, z={:3d}>".format(*pos, *v))

if __name__=="__main__":
    with open("12_three_body/input.txt", 'r') as f:
        positions = process_input(f)

    part1 = simulate(positions)
    print(part1)
