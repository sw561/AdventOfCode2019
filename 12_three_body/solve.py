#!/usr/bin/env python3

import re
from math import gcd
import numpy as np
import numba

def lcm(a, b):
    g = gcd(a, b)
    return a * b // g

def lcm_iter(it):
    x = 1
    for i in it:
        x = lcm(x, i)
    return x

@numba.jit()
def v_diff(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

@numba.jit()
def simulate_1d(positions, t_part1=1000):
    part1 = None
    part2 = None

    start = np.copy(positions)

    t = 0
    while part1 is None or part2 is None:
        t += 1

        # Update velocities first
        for i in range(len(positions)):
            for j in range(len(positions)):
                if j != i:
                    positions[i][1] +=\
                        v_diff(positions[j][0], positions[i][0])

        # Now update positions
        for i in range(len(positions)):
            positions[i][0] += positions[i][1]

        if np.array_equal(positions, start):
            part2 = t

        if t == t_part1:
            part1 = np.copy(positions)

    return part1, part2

def solve(positions, t_part1=1000):

    part1 = []
    part2 = []
    for d_index in range(3):
        pos, period = simulate_1d(np.array(positions[d_index], dtype=int), t_part1=t_part1)
        part1.append(pos)
        part2.append(period)

    # Calculate energy for part 1
    e = 0
    for i in range(len(part1[0])):
        pe = sum(abs(part1[d_index][i][0]) for d_index in range(3))
        ke = sum(abs(part1[d_index][i][1]) for d_index in range(3))
        e += pe * ke

    return e, lcm_iter(part2)

def process_input(f):
    r = re.compile(r'-?\d+')
    positions = []
    for line in f:
        m = r.findall(line)
        positions.append([int(x) for x in m])

    # Want indices to be [dimension][particle_index][s]
    # where s = 0 means position, s = 1 means velocity
    positions = [
        [[positions[i][d], 0] for i in range(len(positions))]
            for d in range(3)]

    # print(positions)
    return positions

def main():
    with open("12_three_body/input.txt", 'r') as f:
        positions = process_input(f)

    part1, part2 = solve(positions)
    print(part1)
    print(part2)

if __name__=="__main__":
    main()
