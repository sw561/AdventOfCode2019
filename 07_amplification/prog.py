#!/usr/bin/env python3

from copy import copy
from itertools import permutations

def decouple(code):
    # Return op-code, and parameter modes

    mode3 = code // 10000
    mode2 = code // 1000 % 10
    mode1 = code // 100  % 10
    op = code % 100

    return op, mode1, mode2, mode3

def read(prog, val, mode):
    if mode == 1:
        # immediate mode
        return val
    elif mode == 0:
        # position mode
        return prog[val]
    else:
        raise Exception("unrecognized mode")

def run(prog, p=0, inp=None):
    while True:
        op, mode1, mode2, mode3 = decouple(prog[p])

        if op in [1,2,7,8]:
            a = read(prog, prog[p+1], mode1)
            b = read(prog, prog[p+2], mode2)
            ret_pointer = prog[p+3]

            if op == 1:
                prog[ret_pointer] = a + b
            elif op == 2:
                prog[ret_pointer] = a * b
            elif op == 7:
                prog[ret_pointer] = int(a < b)
            elif op == 8:
                prog[ret_pointer] = int(a == b)
            else:
                raise Exception("HELP: op = {} not handled".format(op))
            p += 4

        elif op == 3:
            if inp == None:
                # Need to wait for input
                return 'WAIT', (prog, p), None
            else:
                prog[prog[p+1]] = inp
                inp = None
            p += 2

        elif op == 4:
            a = read(prog, prog[p+1], mode1)
            p += 2
            return 'OUT', (prog, p), a

        elif op in [5, 6]:
            a = read(prog, prog[p+1], mode1)
            b = read(prog, prog[p+2], mode2)
            if (op==5 and a) or (op==6 and not a):
                p = b
            else:
                p += 3

        elif op == 99:
            return 'EXIT', (None, None), None

        else:
            raise Exception("Unrecognized op code: {}".format(op))

class ProgramInstance:
    def __init__(self, prog):
        self.prog = copy(prog)
        self.p = 0
        self.status = 'READY'

    def run(self, inp=None):
        # Run until requires input or exits, returns any output values produced
        out = []

        assert (self.status == 'READY') or (self.status == 'WAIT' and inp is not None)

        while True:
            self.status, (self.prog, self.p), o = run(self.prog, self.p, inp)
            inp = None

            if self.status == 'OUT':
                out.append(o)

            if self.status in ['WAIT', 'EXIT']:
                return out

    def __str__(self):
        return self.status

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
