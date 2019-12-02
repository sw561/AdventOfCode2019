#!/usr/bin/env python3

from copy import copy

def run(prog, p=0):
    while True:
        if prog[p] in [1,2]:
            # These are pointers to data, and pointer to memory slot for return value
            a = prog[p+1]
            b = prog[p+2]
            ret = prog[p+3]
            if prog[p] == 1:
                prog[ret] = prog[a] + prog[b]
            elif prog[p] == 2:
                prog[ret] = prog[a] * prog[b]
            p += 4
        elif prog[p] == 99:
            break

def part1(noun, verb):
    p = copy(prog)
    p[1] = noun
    p[2] = verb
    run(p)
    return p[0]

def part2():
    # Find noun and verb s.t part1(noun, verb) == 19690720

    for noun in range(100):
        for verb in range(100):
            if part1(noun, verb) == 19690720:
                return noun, verb

if __name__=="__main__":
    with open("02_program_alarm/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    print(part1(12, 2))

    noun, verb = part2()
    print(100*noun + verb)
