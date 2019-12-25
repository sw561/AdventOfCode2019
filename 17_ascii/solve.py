#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance
from itertools import groupby

new_position_func_dict = {
    "v": lambda x, y: (x,   y+1),
    "^": lambda x, y: (x,   y-1),
    ">": lambda x, y: (x+1, y),
    "<": lambda x, y: (x-1, y),
}

u = ["^", ">", "v", "<"]
turn_right_dict = {u[i-1]: u[i] for i in range(4)}
turn_left_dict = {u[i]: u[i-1] for i in range(4)}

def neighbours(x, y, xmax, ymax):
    for f in new_position_func_dict.values():
        a, b = f(x, y)
        if 0 <= a < xmax and 0 <= b < ymax:
            yield a, b

def alignment_parameters(out):
    xmax = len(out[0])
    ymax = len(out)

    for y in range(ymax):
        for x in range(xmax):
            if out[y][x] == '.':
                continue
            if all(out[b][a] != '.' for a, b in neighbours(x, y, xmax, ymax)):
                yield x * y

def candidate_directions(d):
    yield 'S', d
    yield 'L', turn_left_dict[d]
    yield 'R', turn_right_dict[d]

def find_start(m):
    # Find starting position
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] not in ['.', '#']:
                return x, y

def find_steps(m):
    xmax = len(m[0])
    ymax = len(m)

    x, y = find_start(m)
    d = m[y][x]

    while True:
        for inst, new_d in candidate_directions(d):
            new_x, new_y = new_position_func_dict[new_d](x, y)
            if 0 <= new_x < xmax and 0 <= new_y < ymax and m[new_y][new_x] == '#':
                yield inst
                if inst == 'S':
                    x, y = new_x, new_y
                else:
                    d = new_d
                break

        else:
            break

def find_path(m):
    my_prog = []
    for k, v in groupby(find_steps(m)):
        if k == 'S':
            my_prog.append(sum(1 for _ in v))
        else:
            my_prog.append(k)

    return my_prog

def apply_saving(my_prog, subsequence, sub):
    # print("apply", subsequence, sub)
    for i in range(len(my_prog)-len(subsequence)):
        j = i + len(subsequence)

        if tuple(my_prog[i:j]) == subsequence:
            my_prog = my_prog[:i] + [sub] + my_prog[j:]

    return my_prog

def part2(prog, my_prog, verbose=False):
    prog[0] = 2
    p = ProgramInstance(prog)

    out = p.run()
    for i in out:
        if verbose:
            print(chr(i), end='')

    for i in my_prog:
        if verbose:
            print(i, end='')
        out = p.run(ord(i))
        if verbose:
            for i in out:
                print(chr(i) if i < 128 else i, end='')
        else:
            if p.status == 'EXIT':
                print(out[-1])

def main():
    with open("17_ascii/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    # Part 1
    p = ProgramInstance(prog)
    out = "".join(map(chr, p.run())).split()
    print(sum(alignment_parameters(out)))

    # Reuse map from part 1 to find the path
    path = find_path(out)

    # for i in range(0, len(path), 2):
    #     print(path[i], path[i+1])

    # Gave up - hard-coded solution here :(

    B = ('R', 12, 'L', 12, 'L', 4, 'L', 4)
    path = apply_saving(path, B, 'B')

    C = ('L', 6, 'R', 12, 'R', 8)
    path = apply_saving(path, C, 'C')

    A = ('R', 8, 'R', 12, 'L', 12)
    path = apply_saving(path, A, 'A')
    # print(path)

    my_funcs = "\n".join([
        ",".join(path),
        ",".join(map(str, A)),
        ",".join(map(str, B)),
        ",".join(map(str, C)),
        "n\n",
        ])

    part2(prog, my_funcs, verbose=False)

if __name__=="__main__":
    main()
