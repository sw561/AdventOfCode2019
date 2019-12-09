#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance

def part1(prog, noun, verb):
    prog[1] = noun
    prog[2] = verb
    p = ProgramInstance(prog)
    p.run()
    return p.prog[0]

def part2(prog):
    # Find noun and verb s.t part1(noun, verb) == 19690720

    for noun in range(100):
        for verb in range(100):
            if part1(prog, noun, verb) == 19690720:
                return noun, verb

if __name__=="__main__":
    with open("02_program_alarm/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    print(part1(prog, 12, 2))

    noun, verb = part2(prog)
    print(100*noun + verb)
