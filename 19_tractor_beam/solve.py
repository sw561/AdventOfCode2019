#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance
from collections import deque
from math import atan2, sin, cos, sqrt

def query(x, y):
    p = ProgramInstance(prog)
    out = p.run(x) + p.run(y)
    return out[0]

def part1():
    # m = [[0]*50 for _ in range(50)]
    s = 0
    # Calculate max and min angles of tractor beam
    theta_min = None
    theta_max = None
    for j in range(50):
        for i in range(50):
            if query(i, j):
                # m[j][i] = 1
                s += 1
                if min(i, j) < 10:
                    continue
                theta = atan2(i, j)
                if theta_min is None or theta < theta_min:
                    theta_min = theta
                if theta_max is None or theta > theta_max:
                    theta_max = theta

    # for row in m:
    #     for c in row:
    #         print('#' if c else ' ', end='')
    #     print()

    return s, theta_min, theta_max

def choose_starting_position(theta_min, theta_max):

    # print(theta_max)
    # print(theta_min)

    # print(theta_max*180 / pi)
    # print(theta_min*180 / pi)

    middle_angle = (theta_max + theta_min) / 2

    # cos + sin is width of a square as viewed from an angle.
    #
    # Use small angle approximation for long thin triangle.
    # This is estimate of distance to middle of ship.
    distance_to_ship = (cos(middle_angle) + sin(middle_angle)) * 99 / (theta_max - theta_min)
    
    # To ensure we start search closer to origin than the top left corner
    distance_to_ship -= sqrt(2) * 99

    start_x = int(distance_to_ship * sin(middle_angle))
    start_y = int(distance_to_ship * cos(middle_angle))

    # print(distance_to_ship)
    # print(start_x)
    # print(start_y)

    return start_x, start_y

def neighbours(x, y):
    yield x+1, y
    yield x, y+1
    yield x+1, y+1

def part2(start_x, start_y, theta_min, theta_max):
    # Do bfs away from 0, 0 in positive directions only.
    #
    # Looking for a 100x100 space. (i.e. change in coords is 99x99)
    #
    # Stop when we find a spot in the beam (x, y) where either 
    #   (x-99, y+99) and (x-99, y) are in the beam
    # or
    #   (x+99, y-99) and (x, y-99) are in the beam

    seen = set()
    d = deque([(start_x, start_y)])

    while d:
        pos = d.popleft()

        # print(pos)
        for x, y in neighbours(*pos):
            # print("Candidate ({}, {}) with q = {}".format(x, y, query(x, y)))
            if (x, y) in seen:
                continue

            s = (atan2(x, y) - theta_min) / (theta_max - theta_min)
            if (s < 0.1 or s > 0.9) and not query(x, y):
                continue

            if (x-99, y) in seen and (x-99, y+99) in seen:
                return x-99, y
            if (x, y-99) in seen and (x+99, y-99) in seen:
                return x, y-99

            d.append((x, y))
            seen.add((x, y))

if __name__=="__main__":
    with open("19_tractor_beam/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    s, theta_min, theta_max = part1()
    print(s)
    # print(theta_min, theta_max)

    start_x, start_y = choose_starting_position(theta_min, theta_max)
    # print(start_x, start_y)

    x, y = part2(start_x, start_y, theta_min, theta_max)

    print(x * 10000 + y)
