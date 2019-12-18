#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance, copy

neighbour = {
    1: lambda x, y: (x,   y-1),
    2: lambda x, y: (x,   y+1),
    3: lambda x, y: (x-1, y),
    4: lambda x, y: (x+1, y),
}

inverse_step = {1: 2, 2: 1, 3: 4, 4: 3}

def explore(prog):
    # Use information obtained from prog to construct a map of the surroundings
    m = dict()

    p = ProgramInstance(prog)
    pos = (0, 0)
    steps_from_origin = []

    m[pos] = 'o'

    while True:

        for inp in range(1, 5):
            new_pos = neighbour[inp](*pos)

            if new_pos in m:
                continue

            o = p.run(inp)
            if o[0] == 0:
                m[new_pos] = '#'
                continue

            pos = new_pos
            steps_from_origin.append(inp)
            if o[0] == 1:
                m[new_pos] = ' '
            elif o[0] == 2:
                m[new_pos] = 'X'
                route = copy(steps_from_origin)
                oxygen_pos = new_pos

            break # Go back to beginning of algorithm

        else: # Did not find any interesting moves. Take step towards origin
            if not steps_from_origin:
                break
            last = steps_from_origin.pop()
            o = p.run(inverse_step[last])
            assert o[0] != 0
            pos = neighbour[inverse_step[last]](*pos)

        # display(m)
        # input()

    return m, route, oxygen_pos

def oxygen_fill(m, pos):
    # Do bfs from pos through the map

    m[pos] = 'O'
    nodes = [pos]
    time = -1

    while nodes:
        time += 1

        new_nodes = []
        for node in nodes:

            for inp in range(1, 5):
                new_node = neighbour[inp](*node)
                if m[new_node] in ['#', 'O']:
                    continue

                m[new_node] = 'O'
                new_nodes.append(new_node)

        nodes = new_nodes

        # print("Time: {}".format(time))
        # display(m)
        # input()

    return time

def display(d):
    xmin = min(pos[0] for pos in d.keys())
    xmax = max(pos[0] for pos in d.keys())
    ymin = min(pos[1] for pos in d.keys())
    ymax = max(pos[1] for pos in d.keys())

    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            print(d.get((x, y), '?'), end='')
        print()

if __name__=="__main__":
    with open("15_exploration/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    m, route, oxygen_pos = explore(prog)

    # To display the route
    # pos = (0, 0)
    # for i in route:
    #     pos = neighbour(*pos, i)
    #     m[pos] = '-'
    # display(m)

    print(len(route))

    print(oxygen_fill(m, oxygen_pos))
