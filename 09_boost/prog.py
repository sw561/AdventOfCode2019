#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance

if __name__=="__main__":
    with open("09_boost/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    # Run in test mode - part 1
    p = ProgramInstance(prog)
    o = p.run(1)
    assert len(o) == 1
    print(o[0])

    # Part 2
    p = ProgramInstance(prog)
    o = p.run(2)
    assert len(o) == 1
    print(o[0])
