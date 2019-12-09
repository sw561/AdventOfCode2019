#!/usr/bin/env python3

from itertools import permutations
import sys
sys.path.append('.')
from intcode_computer import ProgramInstance

def simulate(prog, phase_settings):

    amp = [ProgramInstance(prog) for i in range(5)]

    for a, ps in zip(amp, phase_settings):
        a.run(ps)

    value = 0
    for a in amp:
        x = a.run(value)
        assert len(x) == 1
        value = x[0]

    return value

def simulate_feedback(prog, phase_settings):

    amp = [ProgramInstance(prog) for i in range(5)]

    for a, ps in zip(amp, phase_settings):
        a.run(ps)

    value = 0
    while amp[0].status == 'WAIT':
        for a in amp:
            x = a.run(value)
            assert len(x) == 1
            value = x[0]

    return value

def solve(prog):
    return max(simulate(prog, ps) for ps in permutations(range(5)))

def part2(prog):
    return max(simulate_feedback(prog, ps) for ps in permutations(range(5, 10)))

if __name__=="__main__":
    with open("07_amplification/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    print(solve(prog))

    print(part2(prog))
