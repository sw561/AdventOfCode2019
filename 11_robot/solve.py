#!/usr/bin/env python3

import sys
sys.path.append('.')
import intcode_computer
from collections import defaultdict

new_position_func_dict = {
    "v": lambda x, y: (x,   y+1),
    "^": lambda x, y: (x,   y-1),
    ">": lambda x, y: (x+1, y),
    "<": lambda x, y: (x-1, y),
}

u = ["^", ">", "v", "<"]
turn_right_dict = {u[i-1]: u[i] for i in range(4)}
turn_left_dict  = {u[i]: u[i-1] for i in range(4)}

def simulate(prog, start=0):
    p = intcode_computer.ProgramInstance(prog)
    hull = defaultdict(int)
    pos = (0, 0)
    hull[pos] = start
    d = '^'

    while p.status != 'EXIT':
        out = p.run(hull[pos])

        color = out[0]
        turn = out[1]

        hull[pos] = color
        if turn == 0:
            d = turn_left_dict[d]
        else:
            d = turn_right_dict[d]

        pos = new_position_func_dict[d](*pos)

    return hull
            
if __name__=="__main__":
    with open("11_robot/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    hull = simulate(prog)
    print(len(hull))

    hull = simulate(prog, start=1)

    xmin = min(pos[0] for pos in hull.keys())
    xmax = max(pos[0] for pos in hull.keys())
    ymin = min(pos[1] for pos in hull.keys())
    ymax = max(pos[1] for pos in hull.keys())

    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            print('@@' if hull[(x, y)] else '  ', end='')
        print()
