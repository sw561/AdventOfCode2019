#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance
from collections import Counter

def part1(prog):
    # Run in test mode - part 1
    p = ProgramInstance(prog)
    o = p.run()

    d = dict()

    for i in range(0, len(o), 3):
        x = o[i]
        y = o[i+1]
        tile_id = o[i+2]
        d[(x, y)] = tile_id

    count_blocks = Counter(v for k, v in d.items())
    return count_blocks[2]

def calculate_input(ball_position, paddle_position):
    if ball_position[0] > paddle_position[0]:
        return 'l'
    elif ball_position[0] < paddle_position[0]:
        return 'h'
    else:
        return ' '

def run_game(prog):
    p = ProgramInstance(prog)
    d = dict() # display dict
    inp = None

    while p.status != 'EXIT':
        o = p.run(inp)

        for i in range(0, len(o), 3):
            x = o[i]
            y = o[i+1]
            tile_id = o[i+2]
            d[(x, y)] = tile_id
            if tile_id == 4:
                ball_position = (x, y)
            elif tile_id == 3:
                paddle_position = (x, y)

        # display(d)

        if p.status == 'WAIT':
            # inp = input("Move joystick")
            inp = calculate_input(ball_position, paddle_position)
            inp = keypress_map.get(inp, 0)

    return d[(-1, 0)]

character_map = {
    0: ' ',
    1: '@',
    2: '#',
    3: '-',
    4: 'o'
}

keypress_map = {'l': 1, 'h': -1}

def display(d):
    xmin = min(pos[0] for pos in d.keys())
    xmax = max(pos[0] for pos in d.keys())
    ymin = min(pos[1] for pos in d.keys())
    ymax = max(pos[1] for pos in d.keys())

    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            print(character_map.get(d.get((x, y)), '?'), end='')
        print()
    print("score: {}".format(d[(-1, 0)]))

if __name__=="__main__":
    with open("13_arcade/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    print(part1(prog))

    prog[0] = 2

    print(run_game(prog))
