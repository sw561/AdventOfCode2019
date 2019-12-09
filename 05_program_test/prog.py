#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance

def solve(prog, ID):
    p = ProgramInstance(prog)
    out = p.run(ID)
    return out

if __name__=="__main__":
    with open("05_program_test/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    out = solve(prog, 1)
    print(out[-1])
    out = solve(prog, 5)
    print(out[-1])
