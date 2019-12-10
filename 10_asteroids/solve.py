#!/usr/bin/env python3

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
    # los[i] is set of id's of asteroids with line of sight to i
    los = [set() for _ in positions]

    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            dx = x2 - x1
            dy = y2 - y1

            g = gcd(abs(dx), abs(dy))
            if all(m[y1 + k * dy // g][x1 + k * dx // g]=='.' for k in range(1, g)):
                los[i].add(j)
                los[j].add(i)

    return los

def part1(m):
    positions = get_positions(m)

    # print(positions)

    los = los_array(m, positions)

    # print([len(x) for x in los])
    id_max = max(range(len(positions)), key=lambda i: len(los[i]))
    return positions[id_max], len(los[id_max])

if __name__=="__main__":
    with open("10_asteroids/input.txt", 'r') as f:
        m = f.read().strip().split()

    pos, n = part1(m)
    print(n)

