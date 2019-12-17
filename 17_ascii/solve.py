#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance, copy
from itertools import groupby
from collections import Counter

new_position_func_dict = {
    "v": lambda x, y: (x,   y+1),
    "^": lambda x, y: (x,   y-1),
    ">": lambda x, y: (x+1, y),
    "<": lambda x, y: (x-1, y),
}

u = ["^", ">", "v", "<"]
turn_right_dict = {u[i-1]: u[i] for i in range(4)}
turn_left_dict = {u[i]: u[i-1] for i in range(4)}

def neighbours(x, y):
    yield (x,   y-1)
    yield (x,   y+1)
    yield (x-1, y)
    yield (x+1, y)

def checked_neighbours(x, y, xmax, ymax):
    for a, b in neighbours(x, y):
        if 0 <= a < xmax and 0 <= b < ymax:
            yield a, b

def alignment_parameters(out):
    out = out.split()

    out = [list(o) for o in out]

    xmax = len(out[0])
    ymax = len(out)

    for y in range(ymax):
        for x in range(xmax):
            if out[y][x] != '.' and all(out[b][a] != '.' for a, b in checked_neighbours(x, y, xmax, ymax)):
                yield x * y
                out[y][x] = 'O'

    # print("\n".join("".join(o) for o in out))

def part1(prog):
    p = ProgramInstance(prog)
    out = "".join(map(chr, p.run()))

    return out

def my_prog_to_ascii_in(p):
    return [ord(x) for x in p]

def part2(prog, my_prog):
    prog[0] = 2
    p = ProgramInstance(prog)

    out = p.run()
    print("INITIAL MAP=\n{}".format("".join(map(chr, out))))

    for i in my_prog:
        out = p.run(i)
        print("in = {} = {}".format(i, repr(chr(i))))
        if p.status == 'WAIT':
            print("out = {}".format("".join(map(chr, out)).strip()))
        else:
            # out = "".join(map(chr, out))
            # for o in out.split("\n\n"):
            #     print(o)
            #     input()
            print(out)

def candidate_directions(d):
    yield 'S', d
    yield 'L', turn_left_dict[d]
    yield 'R', turn_right_dict[d]

def find_steps(m):
    # Find starting position
    xmax = len(m[0])
    ymax = len(m)
    for y in range(ymax):
        for x in range(xmax):
            if m[y][x] not in ['.', '#']:
                d = m[y][x]
                break
        else:
            continue
        break

    while True:
        for inst, new_d in candidate_directions(d):
            new_x, new_y = new_position_func_dict[new_d](x, y)
            if 0 <= new_x < xmax and 0 <= new_y < ymax and m[new_y][new_x] == '#':
                d = new_d
                yield inst
                if inst == 'S':
                    x, y = new_x, new_y
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

def len_command(c):
    return sum(len(str(ci)) for ci in c)

def subsequences(my_prog):
    # Yield subsequences of the prog
    for i in range(len(my_prog)):
        for j in range(i+1, len(my_prog)+1):
            if any(type(my_prog[x]) is str and my_prog[x] in 'ABC' for x in range(i, j)):
                continue
            if len_command(my_prog[i:j]) < 20:
                yield tuple(my_prog[i:j])

def saving(v, command, verbose=False):
    lc = len_command(command) + len(command)-1

    ret = (lc-1) * (v-1)
    if verbose:
        print("lc", lc)
    return ret

def process(my_prog, let):
    count = Counter(subsequences(my_prog))

    # for c, v in count.items():
    #     if v > 3:
    #         print(c, v)

    cs = sorted(((saving(v, c), str(c), c, v) for c, v in count.items()), reverse=True)

    # for s, _, c, v in cs[:10]:
    #     print(len_command(c), s, c, v)

    if let == 'A':
        choice = 1
    else:
        choice = 0
    s, _, c, v = cs[choice]
    my_prog = apply_saving(my_prog, c, let)

    return my_prog, c

def apply_saving(my_prog, subsequence, sub):
    print("apply", subsequence, sub)
    for i in range(len(my_prog)-len(subsequence)):
        j = i + len(subsequence)

        if tuple(my_prog[i:j]) == subsequence:
            my_prog = my_prog[:i] + [sub] + my_prog[j:]

    return my_prog

def main():
    with open("17_ascii/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    out = part1(prog)
    print(sum(alignment_parameters(out)))
    # print(out)

    m = [list(o) for o in out.split()]
    path = find_path(m)

    # print(path)
    # print("---")
    # path, A = process(path, 'A')
    # path, B = process(path, 'B')

    # # By hand now
    # C = tuple(path[:6])
    # path = ['C'] + path[6:]

    # print(path)
    # print(A)
    # print(B)
    # print(C)

    B = ('R', 12, 'L', 12, 'L', 4, 'L', 4)
    path = apply_saving(path, B, 'B')
    # print(path)

    C = ('L', 6, 'R', 12, 'R', 8)
    path = apply_saving(path, C, 'C')
    # print(path)

    A = ('R', 8, 'R', 12, 'L', 12)
    path = apply_saving(path, A, 'A')
    # print(path)

    MYPROG = "\n".join([
        ",".join(path),
        ",".join(map(str, A)),
        ",".join(map(str, B)),
        ",".join(map(str, C)),
        "n\n",
        ])

    print(MYPROG)

    my_prog_ascii = my_prog_to_ascii_in(MYPROG)
    part2(prog, my_prog_ascii)

if __name__=="__main__":
    main()
