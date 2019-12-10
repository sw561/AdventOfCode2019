#!/usr/bin/env python3

from collections import Counter
from math import atan2

def get_positions(m):
    positions = [] # id -> (x, y) coords
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == '#':
                positions.append((x, y))

    return positions

def gcd(a, b):
    while b != 0:
        a, b = b, a%b 
    return a

def los_array(m, positions):
    # los[i][j] is number of asteroids between the ith and jth asteroid
    # if los[i][j] == 0, then there is direct line of sight between them

    los = [[0]*len(positions) for _ in positions]

    for i in range(len(positions)):
        los[i][i] = None
        for j in range(i+1, len(positions)):
            
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            dx = x2 - x1
            dy = y2 - y1

            g = gcd(abs(dx), abs(dy))
            layer = sum(m[y1 + k * dy // g][x1 + k * dx // g]=='#' for k in range(1, g))
            los[i][j] = layer
            los[j][i] = layer

    return los

def part1(positions, los):
    count, id_max = max((Counter(los[i])[0], i) for i in range(len(positions)))
    return count, id_max

def part2(positions, los, id_max):
    # Sort based on layer and atan2 second. Need -atan2 because angles look like:
    #
    #                    |
    #    atan2 = -3pi/4  |  atan2 = 3pi/4
    #                    |
    #       -------------|------------> x
    #                    |
    #    atan2 = -pi/4   |  atan2 = pi/4
    #                    |
    #                    v
    #                     y
    #
    # So asteroids with larger angles get vaporised first

    pos = positions[id_max]

    def key(i):
        other_pos = positions[i]
        dx = other_pos[0] - pos[0]
        dy = other_pos[1] - pos[1]
        return (los[id_max][i], -atan2(dx, dy))

    vaporised = sorted([x for x in range(len(positions)) if x != id_max], key=key)

    return vaporised

def main(m):
    positions = get_positions(m)
    los = los_array(m, positions)

    count, id_max = part1(positions, los)
    print(count)

    vap = part2(positions, los, id_max)
    (x, y) = (positions[vap[199]])
    print(100*x + y)

if __name__=="__main__":
    with open("10_asteroids/input.txt", 'r') as f:
        m = f.read().strip().split()
    main(m)
